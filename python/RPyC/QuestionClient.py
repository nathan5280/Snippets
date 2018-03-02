import rpyc

conn = rpyc.connect("localhost", 18861)
print(conn.root)
print(conn.root.get_answer)
print(conn.root.the_real_answer_though)