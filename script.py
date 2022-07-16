import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.naver.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["red", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김민서")
write("description", "사대부중 3학년")
write("button", "%")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는거": "고양이, 단거, 영화 등등",
  "싫어하는거": "버섯, 오이 등등",
  "특기사항": "어제 앞머리 잘랐는데 망함",
  "기타": "재밌다, 유치하다, @mallang_rice"
}
information(informations)
