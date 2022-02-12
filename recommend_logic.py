# 점수를 받아서 출력 하는 함수 만들기

# 미리 등록해놓은 커피 데이터
lobster_uganda = [4, 2, 3, 3, 4]
brazil_cerrado = [4, 2, 3, 4, 3]
brazil_kenya = [4, 2, 3, 4, 3]
ethiopia_sidamo = [4, 5, 2, 4, 1]
colombia_supremo = [4, 2, 3, 4, 2]
guatemala = [5, 3, 5, 4, 3]
ethiopia_yirgacheffe = [4, 5, 3, 4, 3]
kenya_AA = [4, 5, 3, 4, 3]

# 사용자가 선택한 결과
body = 4
acidity = 2
sweet = 3
flavor = 3
bitter = 4

result = [body, acidity, sweet, flavor, bitter]
print(result)

if result == lobster_uganda:
    print("로브스타 우간다")
elif result == brazil_cerrado:
    print("브라질 세하도")
elif result == brazil_kenya:
    print("블렌딩")
elif result == ethiopia_sidamo:
    print("시다모")
elif result == colombia_supremo:
    print("콜롬비아 수프리모")
elif result == guatemala:
    print("과테말라")
elif result == ethiopia_yirgacheffe:
    print("에티오피아 예가체프")
elif result == kenya_AA:
    print("케냐AA")
else:
    print("해당되는 결과가 없습니다.")


# 함수로 만들면
def recommend_logic(body, acidity, sweet, flavor, bitter):
    result = [body, acidity, sweet, flavor, bitter]
    print(result)

    if result == lobster_uganda:
        print("로브스타 우간다")
    elif result == brazil_cerrado:
        print("브라질 세하도")
    elif result == brazil_kenya:
        print("블렌딩")
    elif result == ethiopia_sidamo:
        print("시다모")
    elif result == colombia_supremo:
        print("콜롬비아 수프리모")
    elif result == guatemala:
        print("과테말라")
    elif result == ethiopia_yirgacheffe:
        print("에티오피아 예가체프")
    elif result == kenya_AA:
        print("케냐AA")
    else:
        print("해당되는 결과가 없습니다.")


recommend_logic(5, 3, 5, 4, 3)