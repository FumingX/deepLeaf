# in this model, images are only resized directly
# using cifar-10 model structure

from conf import *
import data_reader as data_reader

NB_EPOCHS = 200

train_csv, test_csv = data_reader.load_csv()

# change data augmentation methods here
images = data_reader.load_image_data_resize_directly()
# load train labels (one-hot encoding)
train_labels_orig = data_reader.load_train_labels()

train_feat, test_feat = data_reader.load_pre_extracted_features(standardize=False)

feat_model = Sequential()
feat_model.add(Dense(512, input_dim=192, kernel_initializer='uniform', activation='relu'))
feat_model.add(Dropout(0.3))
feat_model.add(Dense(256, activation='sigmoid'))
feat_model.add(Dropout(0.3))
feat_model.add(Dense(99, activation='softmax'))

feat_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=["accuracy"])

feat_model.count_params()
feat_model.summary()

feat_history = feat_model.fit(train_feat, train_labels_orig,
                              batch_size=16,
                              epochs=200,
                              validation_split=0.1,
                              shuffle=True)

plt.plot(feat_history.history['acc'])
plt.xlabel('Iterations')
plt.ylabel('Training Accuracy')
plt.title('Training Accuracy')
plt.show()

plt.plot(feat_history.history['val_acc'])
plt.xlabel('Iterations')
plt.ylabel('Validation Accuracy')
plt.title('Validation Accuracy')
plt.show()

plt.plot(feat_history.history['acc'])
plt.plot(feat_history.history['val_acc'])
plt.xlabel('Iterations')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
