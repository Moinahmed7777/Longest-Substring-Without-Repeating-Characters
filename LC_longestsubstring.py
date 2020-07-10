# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:40:42 2020

@author: Necro
"""



def maxlen(s):
    my_dict={}
    start_p=0
    maxlength=0
    
    for end_p in range(len(s)):
        if s[end_p] in my_dict:
            start_p= max(start_p,my_dict[s[end_p]]+1)
        my_dict[s[end_p]]=end_p
        maxlength=max(maxlength,end_p + 1 -start_p)
    return maxlength
    
def main():
    s_dict={'pwwkew':3,
            "abcabcbb":3,
            "bbbbb":1}
    for k,v in s_dict.items():
        if maxlen(k)==v:
            print(k," Test for Longest Substring Without Repeating Characters passed! ")
        else:
            print(k," Test for Longest Substring Without Repeating Characters failed :(")
    
    
if __name__ == '__main__':

    main()

