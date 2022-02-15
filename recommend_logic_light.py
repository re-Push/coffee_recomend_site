# 미리 등록해놓은 커피 데이터
lobster_uganda = [2, 3, 3]
brazil_cerrado = [2, 3, 4]
brazil_kenya = [2, 3, 4]
ethiopia_sidamo = [5, 2, 4]
colombia_supremo = [2, 3, 4]
guatemala = [3, 5, 4]
ethiopia_yirgacheffe = [5, 3, 4]
kenya_AA = [5, 3, 4]
indonesia_java =[2, 3, 4]
indonesia_mandeling =[2, 3, 4]
indonesia_bali_kantamani =[2, 3, 4]
indonesia_go_mountain =[4, 3, 4]
indonesia__toraja =[5, 3, 4]
india_monsund_maliva =[4, 4, 5]
colombia_excelso =[5, 3, 5]
guatemala_SHB =[4, 3, 5]
nicaragua_SHB =[4, 3, 3]
mexico_altura_SHB =[3, 3, 4]
elsalvador_pensi_SHB =[3, 3, 4]
costa_rica_SHB =[3, 4, 3]
panama_SHB =[4, 3, 5]
Dominica_AA =[4, 3, 2]
brazil_santos =[3, 3, 4]
brazil_santos_decaffeinated =[3, 3, 4]
honduras_SHG =[4, 2, 3]
peru_HB_GRADE1 =[4, 4, 5]
ethiopia_yirgachev =[5, 3, 4]
mocha_sidamo =[5, 3, 4]
rwanda_AB+ =[3, 3, 2]
malawi_AAA+ =[3, 3, 5]
zimbabwe_AA+ =[5, 3, 4]
tanzania_AA =[5, 3, 4]

# 사용자가 선택한 결과

# 근사화된 커피데이터


#함수

def recommend_logic_apx(acidity, sweet, flavor):
    result = [acidity, sweet, flavor]
    print(result)

    result_approximated = []
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