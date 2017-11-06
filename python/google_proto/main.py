from proto import addressbook_pb2


def main():
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = 'John Deere'
    person.email = 'jdeere@example.com'

    phone = person.phones.add()
    phone.number = '555-1212'
    phone.type = addressbook_pb2.Person.HOME

    print(person)

if __name__ == '__main__':
    main()