if __name__ == "__main__":
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    while True:
        try:
            num_sys = int(input("要转换成的进制："))
            if num_sys >= 37 or num_sys <= 1:
                print("错误的数制")
                continue
            num = int(input("要转换的数值："))
        except ValueError:
            print("请输入数字！")
            continue

        new_num = ""
        while num != 0:
            remainder = int(num % num_sys)  # 将浮点数转为整数
            new_num += nums[remainder]
            num -= remainder
            num /= num_sys

        print(new_num[::-1])
