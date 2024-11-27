class User:
    count_id = 0
    
    def __init__(self, first_name, last_name, gender, membership, remarks):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__membership = membership
        self.__remarks = remarks

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks

