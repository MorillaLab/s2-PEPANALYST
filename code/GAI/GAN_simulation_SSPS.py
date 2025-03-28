"""
S^2-PepAnalyst
"""

# author: Kelly Vomo-Donfack <vomodonfack@math.univ-paris13.fr>
# (C) 2025 Morilla Lab GPLv3

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM, Embedding, Flatten, Dropout, Reshape, Input, Masking
from Bio.Seq import Seq
import random
import tqdm

# standard aminoacid alphabet definition
AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"
MAX_SEQ_LENGTH = 200  # Longitud máxima de los péptidos señal

# Generator of random peptides with variables lengths
def generate_real_peptides(n_samples):
    return [''.join(random.choices(AMINO_ACIDS, k=random.randint(2, MAX_SEQ_LENGTH))) for _ in range(n_samples)]

# Convert sequences into a numeric representation with padding
def encode_peptides(peptides):
    aa_to_index = {aa: i + 1 for i, aa in enumerate(AMINO_ACIDS)}  # 1-based index, 0 para padding
    encoded = [[aa_to_index[aa] for aa in seq] for seq in peptides]
    padded = tf.keras.preprocessing.sequence.pad_sequences(encoded, maxlen=MAX_SEQ_LENGTH, padding='post')
    return np.array(padded)

# Create the generator (Generator)
def build_generator(latent_dim):
    model = Sequential([
        Dense(MAX_SEQ_LENGTH * 64, activation='relu', input_shape=(latent_dim,)),
        Reshape((MAX_SEQ_LENGTH, 64)),
        LSTM(64, return_sequences=True),
        Dense(len(AMINO_ACIDS) + 1, activation='softmax')  # +1 para el padding
    ])
    return model

# Create the discriminator (Discriminator)
def build_discriminator():
    input_layer = Input(shape=(MAX_SEQ_LENGTH, len(AMINO_ACIDS) + 1))
    x = Masking(mask_value=0.0)(input_layer)
    x = LSTM(64, return_sequences=False)(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.3)(x)
    output_layer = Dense(1, activation='sigmoid')(x)
    return Model(input_layer, output_layer)

# Training function for the GAN
def train_gan(generator, discriminator, epochs=10000, batch_size=32, latent_dim=100):
    discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    discriminator.trainable = False
    gan_input = Input(shape=(latent_dim,))
    generated_seq = generator(gan_input)
    gan_output = discriminator(generated_seq)
    gan = Model(gan_input, gan_output)
    gan.compile(optimizer='adam', loss='binary_crossentropy')
    
    real_seqs = encode_peptides(generate_real_peptides(1000))
    real_seqs_one_hot = tf.one_hot(real_seqs, depth=len(AMINO_ACIDS) + 1)
    
    for epoch in tqdm.tqdm(range(epochs), desc="Training Progress"):
        noise = np.random.randn(batch_size, latent_dim)
        fake_seqs = generator.predict(noise)
        
        real_labels = np.ones((batch_size, 1))
        fake_labels = np.zeros((batch_size, 1))
        
        d_loss_real = discriminator.train_on_batch(real_seqs_one_hot[:batch_size], real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_seqs, fake_labels)
        
        noise = np.random.randn(batch_size, latent_dim)
        g_loss = gan.train_on_batch(noise, real_labels)

# Training and generation of simulated signalling peptides
latent_dim = 100
generator = build_generator(latent_dim)
discriminator = build_discriminator()
train_gan(generator, discriminator, epochs=5000, batch_size=32, latent_dim=latent_dim)

# Generate synthetic peptides
noise = np.random.randn(10, latent_dim)
generated_sequences = generator.predict(noise)
generated_sequences = np.argmax(generated_sequences, axis=-1)

# Convert indices into aminoacid sequences removing padding
def decode_sequences(encoded_seqs):
    index_to_aa = {i + 1: aa for i, aa in enumerate(AMINO_ACIDS)}
    return [''.join(index_to_aa.get(aa, '') for aa in seq).rstrip('0') for seq in encoded_seqs]

synthetic_peptides = decode_sequences(generated_sequences)

# Save the output in a file
def save_peptides_to_file(peptides, filename="synthetic_peptides.txt"):
    with open(filename, "w") as file:
        for peptide in peptides:
            file.write(peptide + "\n")

save_peptides_to_file(synthetic_peptides)

