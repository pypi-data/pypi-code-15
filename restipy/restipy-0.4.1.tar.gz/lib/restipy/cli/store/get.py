from restipy.core import LocalStore

def do(args):
    local_store = LocalStore(
        filename=args.save_filename,
        environment=args.environment)

    data = local_store.get_data()
    print data[args.key]
