from smartcache import SmartCache
import tabulate


def main():
    cache = SmartCache()
    print("Welcome to SmartCache 🚀")

    while True:
        print("\nChoose an option:")
        print("1. Add Document")
        print("2. Search Document")
        print("3. List All Documents")
        print("4. Show Search History")
        print("5. Exit")

        while True:
            print("Enter your choice: ", end="")
            try:
                choice = int(input(""))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break

        match choice:
            case 1:
                document = input("Enter your documents: ").strip()
                cache.add_doc(doc=document)
            case 2:
                keyword = input("Enter the keyword: ").strip()
                docs = cache.search_doc(keyword=keyword)
                if isinstance(docs, str):
                    print(docs)
                else:
                    for document in docs:
                        print(document)

            case 3:
                documents = cache.document.get_all_documents()
                if documents:
                    datas = tabulate.tabulate(
                        documents.items(),
                        headers=["document_id", "document"],
                        tablefmt="grid",
                    )
                    print(datas)
                else:
                    print("No documents found")

            case 4:
                while True:
                    print("Get recent N number of queries: ", end="")
                    try:
                        get__recent = int(input())
                    except ValueError:
                        print("Enter a number")
                        continue
                    else:
                        break
                recent = cache.history.get_recent(n=get__recent)

                # Come back later and print this is sorted form by dates
                if recent:
                    for i in recent:
                        print(i)
                else:
                    print("No search history yet")
            case 5:
                print("Exiting SmartCache. Goodbye! 👋")
                break


if __name__ == "__main__":
    main()
