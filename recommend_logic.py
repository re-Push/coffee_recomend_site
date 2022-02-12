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
        print("해당되는 최적의 결과가 없습니다.")


recommend_logic(5, 3, 5, 4, 3)

# 근사값을 추천해주는 로직을 만들어 보았는데요
# 저는 그룹을 3 그룹으로 나누어 봤습니다
# 1,2점 low 그룹, 3점 midium 그룹, 4,5점 high 그룹으로 나누어서 해당하는 커피들을 모두 출력하는 식으로 만들어 보았습니다

# 근사화된 커피데이터
lobster_uganda_apx = ["h", "l", "m", "m", "h"]
brazil_cerrado_apx = ["h", "l", "m", "h", "m"]
brazil_kenya_apx = ["h", "l", "m", "h", "m"]
ethiopia_sidamo_apx = ["h", "h", "l", "h", "l"]
colombia_supremo_apx = ["h", "l", "m", "h", "l"]
guatemala_apx = ["h", "m", "h", "h", "m"]
ethiopia_yirgacheffe_apx = ["h", "h", "m", "h", "m"]
kenya_AA_apx = ["h", "h", "m", "h", "m"]

# 결과값 근사치로 만들기

result_approximated = []
# body
if result[0] <= 2:
    result_approximated.append("l")
elif result[0] == 3:
    result_approximated.append("m")
elif result[0] >= 4:
    result_approximated.append("h")
# acidity
if result[1] <= 2:
    result_approximated.append("l")
elif result[1] == 3:
    result_approximated.append("m")
elif result[1] >= 4:
    result_approximated.append("h")
# sweet
if result[2] <= 2:
    result_approximated.append("l")
elif result[2] == 3:
    result_approximated.append("m")
elif result[2] >= 4:
    result_approximated.append("h")
# flavor
if result[3] <= 2:
    result_approximated.append("l")
elif result[3] == 3:
    result_approximated.append("m")
elif result[3] >= 4:
    result_approximated.append("h")
# bitter
if result[4] <= 2:
    result_approximated.append("l")
elif result[4] == 3:
    result_approximated.append("m")
elif result[4] >= 4:
    result_approximated.append("h")

print(result_approximated)

# 비슷한 결과 출력
if result_approximated == lobster_uganda_apx:
    print("로브스타 우간다")
if result_approximated == brazil_cerrado_apx:
    print("브라질 세하도")
if result_approximated == brazil_kenya_apx:
    print("블렌딩")
if result_approximated == ethiopia_sidamo_apx:
    print("시다모")
if result_approximated == colombia_supremo_apx:
    print("콜롬비아 수프리모")
if result_approximated == guatemala_apx:
    print("과테말라")
if result_approximated == ethiopia_yirgacheffe_apx:
    print("에티오피아 예가체프")
if result_approximated == kenya_AA_apx:
    print("케냐AA")


# 함수로 만들면
def recommend_logic_apx(body, acidity, sweet, flavor, bitter):
    result = [body, acidity, sweet, flavor, bitter]
    print(result)

    result_approximated = []
    # body
    if result[0] <= 2:
        result_approximated.append("l")
    elif result[0] == 3:
        result_approximated.append("m")
    elif result[0] >= 4:
        result_approximated.append("h")
    # acidity
    if result[1] <= 2:
        result_approximated.append("l")
    elif result[1] == 3:
        result_approximated.append("m")
    elif result[1] >= 4:
        result_approximated.append("h")
    # sweet
    if result[2] <= 2:
        result_approximated.append("l")
    elif result[2] == 3:
        result_approximated.append("m")
    elif result[2] >= 4:
        result_approximated.append("h")
    # flavor
    if result[3] <= 2:
        result_approximated.append("l")
    elif result[3] == 3:
        result_approximated.append("m")
    elif result[3] >= 4:
        result_approximated.append("h")
    # bitter
    if result[4] <= 2:
        result_approximated.append("l")
    elif result[4] == 3:
        result_approximated.append("m")
    elif result[4] >= 4:
        result_approximated.append("h")

    print(result_approximated)

    if result_approximated == lobster_uganda_apx:
        print("로브스타 우간다")
    if result_approximated == brazil_cerrado_apx:
        print("브라질 세하도")
    if result_approximated == brazil_kenya_apx:
        print("블렌딩")
    if result_approximated == ethiopia_sidamo_apx:
        print("시다모")
    if result_approximated == colombia_supremo_apx:
        print("콜롬비아 수프리모")
    if result_approximated == guatemala_apx:
        print("과테말라")
    if result_approximated == ethiopia_yirgacheffe_apx:
        print("에티오피아 예가체프")
    if result_approximated == kenya_AA_apx:
        print("케냐AA")
    print("근사한 결과값을 구해봤어요")


# 함수 결과값 출력
recommend_logic_apx(5, 5, 3, 5, 3)

# 데이터가 부족한 건지 조금더 근사한 수치로 구해야하는건지 아직 최선의 결과를 도출해 내는 작업에 대해서 고민을 해봐야할 것 같아요