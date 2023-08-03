import streamlit as st

st.title('불쏘시개 상권정보도우미')

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

OPENAI_API_KEY = "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"

chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY
)

text1 = "이제부터 너는 상권 분석 전문가로서, 내가 제시해준 분석데이터에 기반해서, 자영업자들에게  도움되는 조언을 하는 역할을 할 거야. 너의 역할을 이해해?"
text2 = "평균 매출액, 평균 유동인구, 평균 월세, 상권 주요 키워드, 매출트렌드, 성장가능성 등을 입력된 데이터를 기반으로 상권분석 보고서를 나에게 제공해줘"
text3 = 내가 분석한 식당은 부산대학교 인근에 위치한 델라고이고, 델라고의 업종은 양식입니다. 상권분석결과 주변 상권은 월평균 1549만원의 매출을 올렸으며, 이것은 전월대비 1.1% 성장한 수치야. 그리고 월평균 매출 건수는 전월 대비 3.5프로 증가한 675건이야. 일 평균 유동인구는 62000명이며, 수요일에 가장 많은 유동인구를 가져. 또한, 남자가 여자보다 약 14%많은 매출에 기여하고, 현재 안정성은 안전 등급으로 판단되며, 지속적 성장이 기대됩니다. 하지만 양식이 아닌 전체 음식 대분류로 가게 됐을때는 정체가능성이 있다고 판단이됩니다. 평균 임대료는 평당 45,000원으로 보입니다. 이 정보들을 기반으로 분석보고서를 작성해줘"

def send_click(chat,prompt):
    messages = [SystemMessage(content=text1,text2,text3),HumanMessage(content=prompt)
]
    response = chat(messages).content
    return response    

def main():
    st.title('Ask ChatGPT')
    user_input = st.text_input("Question: ", key='prompt')
    if st.button("Send"):
        response = send_click(chat, user_input)
        st.subheader("Answer: ")
        st.success(response, icon= "👍")

if  __name__ == '__main__':   
    main()
