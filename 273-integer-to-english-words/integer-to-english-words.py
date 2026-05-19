class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        num_word_one = {}
        num_word_one[1] = "One"
        num_word_one[2] = "Two"
        num_word_one[3] = "Three"
        num_word_one[4] = "Four"
        num_word_one[5] = "Five"
        num_word_one[6] = "Six"
        num_word_one[7] = "Seven"
        num_word_one[8] = "Eight"
        num_word_one[9] = "Nine"

        num_word_middle = {}
        num_word_middle[10] = "Ten"
        num_word_middle[11] = "Eleven"
        num_word_middle[12] = "Twelve"
        num_word_middle[13] = "Thirteen"
        num_word_middle[14] = "Fourteen"
        num_word_middle[15] = "Fifteen"
        num_word_middle[16] = "Sixteen"
        num_word_middle[17] = "Seventeen"
        num_word_middle[18] = "Eighteen"
        num_word_middle[19] = "Nineteen"
        num_word_middle[2] = "Twenty"
        num_word_middle[3] = "Thirty"
        num_word_middle[4] = "Forty"
        num_word_middle[5] = "Fifty"
        num_word_middle[6] = "Sixty"
        num_word_middle[7] = "Seventy"
        num_word_middle[8] = "Eighty"
        num_word_middle[9] = "Ninety"

        hundred = False
        thousand = False
        million = False
        billion = False

        total_output = ""
        while num:
            output = ""
            first = num % 10
            num = num // 10
            second = num % 10
            num = num // 10
            third = num % 10
            num = num // 10

            if third != 0:
                output = output + num_word_one[third] + " Hundred "
            if second == 1:
                val = (second * 10) + first
                output = output + num_word_middle[val] + " "
                first = 0
            elif second != 0:
                output = output + num_word_middle[second] + " "
            if first != 0:
                output = output + num_word_one[first] + " "
            
            if million:
                if output != "":
                    output += "Billion "
                billion = True
            elif thousand:
                if output != "":
                    output += "Million "
                million = True
            elif hundred:
                if output != "":
                    output += "Thousand "
                thousand = True
            else:
                hundred = True

            total_output = output + total_output
        if total_output[-1] == " ":
            return total_output[:-1]
        else:
            return total_output

        