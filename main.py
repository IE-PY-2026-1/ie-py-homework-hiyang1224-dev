# 파일이름 :
# 작 성 자 :
import builtins
print = builtins.print

name = "양영서"
tax_rate = 0.033
total_points = 0

print(f"--- {name}의 알바 급여 관리 시스템 ---")
print("현재 선택 가능한 작업 카테고리:")
print(categories)
print("-" * 40)

print("알파벳으로 작업 종류를 선택하세요 (A~G):")
choice = input("선택: ")

if choice == 'A':
    work_name = categories[0]
    file_price = 600
    ques_price = 20
elif choice == 'B':
    work_name = categories[1]
    file_price = 500
    ques_price = 30
elif choice == 'C':
    work_name = categories[2]
    file_price = 400
    ques_price = 40
elif choice == 'D':
    work_name = categories[3]
    file_price = 300
    ques_price = 50
elif choice == 'E':
    work_name = categories[4]
    file_price = 200
    ques_price = 50
elif choice == 'F':
    work_name = categories[5]
    file_price = 70
    ques_price = 0
elif choice == 'G':
    work_name = categories[6]
    file_price = 100
    ques_price = 0
else:
    print("잘못된 카테고리입니다. 프로그램을 다시 실행해 주세요.")
    work_name = "미선택"


if work_name != "미선택":
    f_count = int(input(f"작업한 파일 개수: "))
    q_count = int(input(f"작업한 문항 수: "))
    current_points = (f_count * file_price) + (q_count * ques_price)
    total_points += current_points
    tax_amount = total_points * tax_rate
    final_salary = total_points - tax_amount


    print("\n" + "="*40)
    print(f" [ 작업 보고서: {work_name} ]")
    print(f" - 이번 작업 급여: {current_points}원")
    print(f" - 누적 합계 급여: {total_points}원")
    print("-" * 40)

    # 독립 if문 활용
    if total_points > 0:
        print(f" 공제 세금(3.3%): {tax_amount:.1f}원")
        print(f" 최종 예상 수령액: {final_salary:.1f}원")

    print("="*40)