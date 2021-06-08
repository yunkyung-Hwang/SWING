import random   # random 함수를 위한 import

def openFile():     # 점수 파일을 불러오는 함수
    f=open("C:/Users/dudhk/OneDrive/바탕 화면/황윤경/SWING/python-UP&DOWN.txt","r")
    lines=f.readlines()
    for i in range(0,len(lines)):
        fileSplit=lines[i].split(" : ")
        names.append(fileSplit[0])
        score.append(int(fileSplit[1]))
    f.close()
    

def storeScore():   # 이름과 점수를 저장하는 함수
    f=open("C:/Users/dudhk/OneDrive/바탕 화면/황윤경/SWING/python-UP&DOWN.txt","w")
    for i in range(len(score)):
        f.write(names[i]+" : "+str(score[i])+"\n")
    f.close()

score = []      # 순위 확인을 위한 스코어 리스트
names = []       # 닉네임을 입력 받기 위한 이름 리스트

print("Up & Down 게임에 오신 것을 환영합니다 !")    # 게임 시작시에만 나오는 문구

openFile()  # 프로그램 시작시 점수 파일을 불러옴

while True:
    # 매 게임마다 정답이 바뀌어야하기 때문에 반복문 안에 변수 생성
    answer = random.randint(1,100)  # 1~100 사이의 랜덤한 정답 생성
    # min ~ max 사이의 숫자 입력
    min = 1
    max = 100
    count = 0   # 몇 번째 시도인지 알려주는 변수


    print("정답 : %d" % answer)     # 게임 테스트를 수월하게 하기 위한 답

    print("1.게임시작  2.기록확인  3.게임종료")
    remote = int(input(">>"))   # 어떤 행동을 취할 것인지 입력받는 리모컨

    if remote == 3:     # 게임 종료를 선택할 경우 while문 탈출
        print("게임을 종료합니다.")
        storeScore()    # 게임 종료시 그동안의 게임 기록을 저장
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
                        print("최고기록 갱신~!\n")
                        score.append(count)
                        name = input("닉네임을 입력하세요 : ")
                        names.insert(0,name)

                        break
                    elif score[0] > count:  # 두번째 이상 시도에서 최고기록을 달성했을 경우
                        print("최고기록 갱신~!\n")
                        score.append(count)
                        score.sort()
                        name = input("닉네임을 입력하세요 : ",)
                        names.insert(0,name)

                        break
                    else:   # 두번째 이상 시도에서 최고기록을 달성하지 못했을 경우
                        ''' [2번 수정부분] - 모든 참가자들이 기록에 남는다고 착각함
                        score.append(count)
                        score.sort()
                        '''
                        print()
                        break


        elif remote == 2:   # 기록 확인을 선택할 경우
            print("rank/name/score")
            for i in range(0,len(score)):
                print("%d %s %d" % (i+1, names[i], score[i]))
            print()
            break
