def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music

def solution(m, musicinfos):
    answer = []
    
    for i in range(len(musicinfos)):
        start, end, title, music=musicinfos[i].split(",")
        music = change(music)
        m = change(m)
        s_hour,s_minute = map(int,start.split(":"))
        e_hour,e_minute = map(int,end.split(":"))
        if e_hour - s_hour ==0:
            minute = e_minute - s_minute
        else:
            minute = 60*(e_hour-s_hour) + e_minute - s_minute
        music*=(minute//len(music))+1
        music = music[:minute]
    
        if m in music:
            answer.append([title,minute])
    if len(answer) !=0:
        answer = sorted(answer, key = lambda x: (-x[1],x[0]))
        answer = answer[0][0]
    if answer == []:
        answer ="(None)"
        return answer 
    return answer
