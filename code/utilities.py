from libs import *
from tensorflow.keras.callbacks import ModelCheckpoint


def readFastaFiles(filename):
    f=open(filename,'r')
    labels=[]
    seqs=[]
    str= ""
    label = ""
    for line in f.readlines():
        data = line.rstrip()  
        index = data.__contains__('>')
        if index == True: 
            #201 because we are counting . and we are going to remove it
            if len(str) > 0 and len(str) <= 201:
                labels.append(label)
                seqs.append(str.replace('*', ''))
            str= ""
            label = ""
            label+=data
        else:  
            str+=data

    if len("".join(str))<= 201:
        labels.append(label)
        seqs.append(str.replace('*', ''))
    f.close()
    return labels,seqs   


def createFaster(filename,labels,sequences):
    with open(filename, 'w') as f:
        # Write content to the file
        for i in range(len(labels)):
        # for i in range(5):
            f.write(labels[i]+"\n")
            f.write(sequences[i]+"\n")


#Creating a file of all signalP sequences
#getting supposed signalprotein
def signalProtein(filename,resultSignalp,sequences,labels):
    new_label = []
    new_sequence = []
    i = 0
    with open(filename, 'w') as f:
        for r in result_signalp:
            if r > 0 and r < 0.7:
                new_label.append(0)
            elif r > 0.7:
                new_label.append(1)
            if r > 0:
                f.write(labels[i]+"\n")
                f.write(sequences[i]+"\n")
                new_sequence.append(sequences[i])
            i+=1
    return new_label,new_sequence         


def resultSignalP(filename):
    f=open(filename,'r')
    result=[]
    next(f)
    next(f)
    for line in f.readlines():
        data = line.rstrip()  
        index = data.split("\t")[1].__contains__('SP')
        if index == True: 
            result.append(1)
        else:
            result.append(0)
    f.close()
    return result  


def geotop_analysis(data):
    # U_train = U_train_b + U_train_m + U_test_b + U_test_m
    n = 100
    i = 0
    dgms_tda = []
    dgms_per_var = []
    dgms_per_linalg = []
    for U in data:
        print(i)
        L = np.linspace(np.min(U), np.max(U),  n)[::-1]

        life, barecode, persistence, connected_comp, Per_total, Area_total, euler_total, per, area, euler = function_persistance(U, L, False)
        diagram_pondere_total_vari = np.zeros((len(life), 2))
        diagram_pondere_linalg = np.zeros((len(life), 2))
        diagram = np.zeros((len(life), 2))
        k = 0
        idx_keys = list(life.keys())
        for idx in idx_keys[1:]:
            diagram_pondere_total_vari[k][0] = (np.sum(per[idx]))*life[idx][1]
            diagram_pondere_total_vari[k][1] = (np.sum(per[idx]))*life[idx][0]
            diagram_pondere_linalg[k][0] = (np.linalg.norm(per[idx]))*life[idx][1]
            diagram_pondere_linalg[k][1] = (np.linalg.norm(per[idx]))*life[idx][0]
            diagram[0] = life[idx][1]
            diagram[1] = life[idx][0]
            k=k+1
        dgms_tda.append(diagram)
        dgms_per_linalg.append(diagram_pondere_linalg)
        dgms_per_var.append(diagram_pondere_total_vari)
        i=i+1
    return dgms_per_linalg


def concate_embedding_geotop(embedding,dgms,dim):
    len_data = max(array.shape[0] for array in dgms)
    long = embedding.shape[1]
    res = []
    i = 0
    for array in dgms:
        flat = array.flatten()
        #flatten and concatenate the rest with zeroes
        t = dim - (long + flat.shape[0])
        res.append(np.concatenate((np.concatenate((embedding[i], flat)), np.zeros(t))))
    return res


def model_trainning_saving(shape,epoch,model_name,train_data,train_labels,test_data,test_labels):
    model = Sequential()

    model.add(Conv2D(filters=8, kernel_size=(3, 3), padding="same",activation='relu', input_shape=(shape[0],shape[1],1)))
    model.add(layers.AveragePooling2D())
    
    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), padding="same",activation='relu'))
    model.add(layers.AveragePooling2D())
    
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3),padding="same", activation='relu'))
    model.add(layers.AveragePooling2D())
    
    
    model.add(layers.Flatten())
    
    model.add(layers.Dense(units=128, activation='relu',kernel_regularizer=regularizers.l2(1e-4),bias_regularizer=regularizers.l2(1e-4), activity_regularizer=regularizers.l2(1e-5)))
    
    model.add(layers.Dense(units=64, activation='relu',kernel_regularizer=regularizers.l2(1e-4),bias_regularizer=regularizers.l2(1e-4),activity_regularizer=regularizers.l2(1e-5)))
    
    model.add(layers.Dense(units=1, activation = 'sigmoid',kernel_regularizer=regularizers.l2(1e-4),bias_regularizer=regularizers.l2(1e-4),activity_regularizer=regularizers.l2(1e-5)))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    print(model.summary())
    checkpoint = ModelCheckpoint(
        model_name+'.keras',          
        monitor='val_accuracy',          # what to monitor (val_loss or val_accuracy)
        save_best_only=True,         
        mode='min',                  
        verbose=1
    )
    
    history = model.fit(x=train_data, y=train_labels,epochs=epoch,shuffle=True,validation_data=(test_data, test_labels),verbose=1,batch_size=64,callbacks=[checkpoint])

    print(history.history)
    df = pd.DataFrame(history.history)

    df.to_csv(model_name+'_history.csv', index=False)

    plt.plot(history.history['accuracy'], label='training data')
    plt.plot(history.history['val_accuracy'], label='validation data')
    plt.ylabel('Accuracy')
    plt.xlabel('No. epoch')
    plt.legend(loc="lower right")
    plt.savefig(model_name+".png", dpi=300)
    plt.show()


def concate_embedding_geotop(embedding,dgms,dim):
    # len_data = max(array.shape[0] for array in dgms)
    long = embedding.shape[1]
    res = []
    i = 0
    for array in dgms:
        flat = array.flatten()
        #flatten and concatenate the rest with zeroes
        t = dim - (long + flat.shape[0])
        res.append(np.concatenate((np.concatenate([embedding[i], flat]), np.zeros(t))))
        i +=1
    return res


def concat_embedding_geotop(dgms,dim):
    # len_data = max(array.shape[0] for array in dgms)
    res = []
    for array in dgms:
        flat = array.flatten()
        #flatten and concatenate the rest with zeroes
        t = dim - flat.shape[0]
        res.append(np.concatenate([flat, np.zeros(t)]))
    return res


def tape_embedding(sequence):
    len_data = len(sequence)
    num_of_features = 768
    embedded=np.zeros((len_data,num_of_features))
    y=np.zeros(len_data)
    
    
    # now lets populate X
    i=0
    for s in sequence:
        #tape
        print(i)
        token_ids = torch.tensor([tokenizer_tape.encode(s)])
        output = model_tape(token_ids)
        sequence_output = output[0]
        # print(len(np.mean(sequence_output.detach().numpy(),axis=1)))
        # val = np.append(np.array(np.mean(sequence_output.detach().numpy(),axis=1)),new_label[i])
        embedded[i]= np.array(np.mean(sequence_output.detach().numpy(),axis=1) )
    
        #transformers
        i=i+1
    return embedded
