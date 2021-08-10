def solution(strs):
    diction = {
        "zero" : "0", "one" : "1", "two" : "2",
        "three" : "3", "four" : "4", "five" : "5",
        "six" : "6", "seven" : "7", "eight" : "8",
        "nine" : "9"
    };
    
    arr = []; 		
    string = "";	
    
    for s in strs:
        if s.isalpha():		
            string += s;
            
            if string in diction: 
                arr.append(diction[string]); 
                string = "";
        else:
            arr.append(s);

	
    answer = int("".join(arr));	
    return answer;