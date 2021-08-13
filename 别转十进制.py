if __name__ == "__main__":
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    while True:
        try:
            num_sys = int(input("被转换的进制（2~36）："))
            if num_sys >= 37 or num_sys <= 1:
                print("错误的数制")
                continue

            num = input("要转换的数值：")
            new_num = 0

            ws = len(num) - 1
            for t in num:  # 检查输入的数是否正确
                if t not in nums[:num_sys]:
                    raise ValueError
                else:  # 如果正确，将 new_num 的值加上(这个数位对应的十进制值与对应位权的积)
                    wq = num_sys ** ws  # 计算当前数位的位权
                    ws -= 1

                    ten = wq * nums.index(t)  # 计算当前位对应的十进制值
                    new_num += ten
        except ValueError:
            print("请输入正确数字！")
            continue

        print(new_num)
