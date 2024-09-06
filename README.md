# Card Recommendation Homepage
카드 추천 홈페이지
[Demo](https://9511dasol.github.io/Card-for-react/) <- 제작중 ( 메인, 카드 찾기)

github: https://github.com/9511dasol/Card-for-react

2024-08-05: userNavbar (구현)

2024-08-07: Main 화면 

2024-08-09: 카드찾기

2024-08-12: FAQ, 1:1 문의하기

2024-08-13: 인기카드 

2024-08-16~17: 관리자 페이지(navbar, 카드 등록)

2024-08-20: 관리자 페이지(faq 및 1:1 문의 페이지)

2024-08-21: 관리자 페이지(faq 추가 컨텐츠)

2024-08-25: 간단한 버그 픽스

2024-08-~ ing: 반응형 웹페이지 구현중

2024-09-06: navbar에 한해서 반응형 컨포넌트 구현

## 프로젝트 소개 🖥️
자연어 처리를 활용하여 만든 카드 추천 홈페이지 입니다.

2024.08.05 ~  React, TypeScript, Redux +@를 이용하여 프론트엔드 위주로 사이트 개편예정
## 개발 기간 ⏱️
23.03.10 - 23.12.16

24.08 - ing
### 맴버 구성 🧑‍🤝‍🧑
- 한다솔: 프론트앤드(메인), 백앤드(보조, 자연어처리, 데이터베이스, 서버 담당)
- 우재현: 백엔드(특정 커뮤니티 게시글, 댓글 크롤링)

### 개발 환경 ⚙️
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## 주요 기능 📌
- 텐서플로우를 이용한 자연어 처리 모델 개발 - 특정 커뮤니티에 올라오는 게시글 댓글 학습
- 최근(하루)에 많이 언급된 카드 순으로 나열해주는 알고리즘 구현
- 특정 카드 url을 넣으면 카드 이름, 혜택, 연회비 등 정보를 자동으로 가져오는 크롤링&알고리즘 구현
- 포인트 / 할인 카드 검색 기능 구현

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
        print("{:.2f}% 확률로 긍정 글입니다.\n".format(score * 100))
      else:
        print("{:.2f}% 확률로 부정 글입니다.\n".format((1 - score) * 100))
    sentiment_predict('레이디 클레식 카드 좋다~~') # 95.01% 확률로 긍정 글입니다.
    sentiment_predict('더모아 사기네 ?') # 95.01% 확률로 긍정 글입니다.
### jQuery
    let innate_number = $(button).parents('#id or .class'). - 부모의 값 가져요기
    let innate_number = $(button).siblings('.IN').text(); # 자기 형제
    let innate_number = $(button).attr('value') # 속성 값 # 자기 자신 속성값
    let innate_number = $(button).text() # 자시 자신 text
    
