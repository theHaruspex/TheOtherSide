class DialogueTree:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.current_node = "start"

    def get_current_node_text(self):
        return self.adj_list[self.current_node]["text"]

    def get_current_node_options(self):
        return list(self.adj_list[self.current_node]["options"].keys())

    def select_option(self, option):
        if option in self.adj_list[self.current_node]["options"]:
            self.current_node = self.adj_list[self.current_node]["options"][option]
            return True
        else:
            return False
