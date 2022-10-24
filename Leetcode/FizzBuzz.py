class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        stringArr = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                stringArr.append("FizzBuzz")
            elif i % 3 == 0:
                stringArr.append("Fizz")
            elif i % 5 == 0:
                stringArr.append("Buzz")
            else:
                stringArr.append(str(i))
        return stringArr
