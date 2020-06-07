import random   # random 함수를 위한 import

score = []      # 순위 확인을 위한 스코어 리스트

print("Up & Down 게임에 오신 것을 환영합니다 !")    # 게임 시작시에만 나오는 문구

while True:
    # 매 게임마다 정답이 바뀌어야하기 때문에 반복문 안에 변수 생성
    answer = random.randint(1,100)  # 1~100 사이의 랜덤한 정답 생성
    # min ~ max 사이의 숫자 입력
    min = 1
    max = 100
    count = 0   # 몇 번째 시도인지 알려주는 변수

    # print("정답 : %d" % answer)     # 게임 테스트를 수월하게 하기 위한 답

    print("1.게임시작  2.기록확인  3.게임종료")
    remote = int(input())   # 어떤 행동을 취할 것인지 입력받는 리모컨

    if remote == 3:     # 게임 종료를 선택할 경우 while문 탈출
        print("게임을 종료합니다.")
        break
    
    while True:
        if remote == 1: # 게임 시작을 선택할 경우
            if count > 9:  # 입력 시도가 10번이 넘었을 경우     [3번 수정부분] count가 0부터 시작하기에 0~9로 10번 기회
                print("입력 횟수를 초과하였습니다. 게임오버!\n")
                break
            else:   # 입력 시도가 10번 이하일 경우
                print("%d번째 숫자 입력 (%d ~ %d) : " % (count+1, min, max), end='')
                num = int(input())  # 사용자에게 정답을 입력받음

                # [1번 수정 전 부분] - 정답을 입력받을때마다 시도횟수 증가라고 착각함
                # count += 1

                if num < answer and num >= min: # 입력값이 정답 미만 최솟값 이상일 경우
                    print("Up")
                    min = num + 1   # 최솟값을 입력값보다 1큰 값으로 초기화 
                    count += 1      # [1번 수정부분] 입력값이 범위 사이일 경우에만 시도횟수 증가
                elif num > answer and num <= max:   # 입력값이 정답 초과 최댓값 이하일 경우
                    print("Down")
                    max = num - 1   # 최댓값을 입력값보다 1작은 값으로 초기화
                    count += 1      # [1번 수정부분] 입력값이 범위 사이일 경우에만 시도횟수 증가
                elif num > max or num < min:    # 입력값이 범위 밖의 수일 경우
                    print("범위 안의 숫자가 아닙니다. 다시 입력해주세요")
                elif num == answer:     # 입력값이 정답일 경우
                    count += 1      # [1번 수정부분] 입력값이 범위 사이일 경우에만 시도횟수 증가
                    print("정답입니다!")
                    print("%d번 만에 맞추셨습니다" % count)

                    if not score:   # 첫 시도 (score리스트에 아무 값도 저장되어있지 않는 경우)
                        score.append(count)
                        print("최고기록 갱신~!\n")
                        break
                    elif score[0] > count:  # 두번째 이상 시도에서 최고기록을 달성했을 경우
                        score.append(count)
                        score.sort()
                        print("최고기록 갱신~!\n")
                        break
                    else:   # 두번째 이상 시도에서 최고기록을 달성하지 못했을 경우
                        ''' [2번 수정부분] - 모든 참가자들이 기록에 남는다고 착각함
                        score.append(count)
                        score.sort()
                        '''
                        print()
                        break


        elif remote == 2:   # 기록 확인을 선택할 경우
            for i in range(0,len(score)):
                print("%d등 : %d" % (i+1, score[i]))
            print()
            break
