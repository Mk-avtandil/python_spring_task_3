class Find_max_elem:
    def find_max_elem(self, my_list):
        max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
