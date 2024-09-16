def titleToNumber(self, columnTitle: str) -> int:
        le= len(columnTitle)
        ret=0
        for count, value in enumerate(columnTitle):
            print(count,ord(value)-64)
              
            ret = ret + 26**(le-count-1)* (ord(value)-64)
            print(ret)
        return(ret)
