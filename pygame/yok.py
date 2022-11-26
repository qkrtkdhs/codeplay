words = ["ㄴㄱㅁ", "시발", "ㅄ", "병신", "ㅂㅅ", "새끼",  "새끼", "홍어", "일베", "씨발"]
chat = 0
bads = 0
newyok = 0
while True:
    chat = input("코딩쌤 = ")
    bads = 0
    if chat == "관리자":
        newyok = input("[새 금칙어] : ")
        words.append(newyok)
        print(f"[금칙어 {newyok} 추가]")
        print(words)
        continue
    for bad in words:
        if bad in chat:
            bads += 1
    if bads > 0:
        print(f"[금지어 {bads}개. 채팅 1개월 압수]")
    else:
        print(chat)
