# Card Recommendation Home Page
카드 추천 홈페이지

## 프로젝트 소개 🖥️
자연어 처리를 활용하여 만든 카드 추천 홈페이지 입니다.

## 개발 기간 ⏱️
23.03.10 - 23.12.16

### 맴버 구성 🧑‍🤝‍🧑
- 한다솔: 프론트앤드, 백앤드(자연어처리, 데이터베이스, 서버 담당)
- 우재현: 중도포기
- 이강성: 중도포기

### 개발 환경 ⚙️
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)


![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)


## 주요 기능 📌
- DB값 검증
- 자연어처리(AI)

# 주요 코드
### Python
    from tensorflow.keras.layers import Embedding, Dense, LSTM, GRU
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.callbacks import EarlyStopping
    embedding_size = 248# 일반적으로 100에서 300
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4, restore_best_weights=True)
    model = Sequential()
# 임베딩층 추가
    model.add(Embedding(input_dim=num_words,      # 사용하는 단어의 개수
                        output_dim=embedding_size,# 임베딩 차원
                        input_length=max_tokens,  # 리뷰의 길이
                        name='layer_embedding'))
    model.add(LSTM(units=256)) # GRU나 LSTM 사용 (여기에서는 LSTM이 좀 더 좋은 성능을 보이는 것 같음)
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    model.fit(X_train, y_train, epochs=10000, callbacks=es, batch_size=64, validation_split=0.2)
    def sentiment_predict(new_sentence):
      new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence) # 한글과 공백만 남기기
      new_sentence = okt.morphs(new_sentence, stem=True) # 형태소 분석
      new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
      encoded = tokenizer.texts_to_sequences([new_sentence]) # 토큰화
      pad_new = pad_sequences(encoded, maxlen = max_tokens) # 패딩
      score = float(model.predict(pad_new)) # 예측
      if(score > 0.5):
        print("{:.2f}% 확률로 긍정 댓글입니다.\n".format(score * 100))
      else:
        print("{:.2f}% 확률로 부정 댓글입니다.\n".format((1 - score) * 100))
    sentiment_predict('레이디 클레식 카드 좋다~~') # 95.01% 확률로 긍정 댓글입니다.
    sentiment_predict('더모아 사기네 ?') # 95.01% 확률로 긍정 댓글입니다.
### JAVASCRIPT

    
