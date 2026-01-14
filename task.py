

class Task:
    # had dala hiya li kat7km f l9iyam li hkayakhwd l class fach hkatstad3ih 
    def __init__(self,title,description,isDone=False):

        # hna kan3rf ana dok l9iyam li dakhla li f dik __init__ kanrbtha b lkain li ghaytncha 
        self.title = title
        self.description = description
        self.isDone = isDone
    

    def sho_info(self):
        print(f"title : {self.title}")
        print(f"description : {self.description}")
        print(f"status : {self.isDone}")