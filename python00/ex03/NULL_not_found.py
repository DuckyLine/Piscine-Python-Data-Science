def NULL_not_found(object: any) -> int:
	match object:
		case None:
			print(f"Nothing: {object} {type(object)}")
		case float() if object != object:
			print(f"Cheese: {object} {type(object)}")
		case False:
			print(f"Fake: {object} {type(object)}")
		case 0:
			print(f"Zero: {object} {type(object)}")
		case "":
			print(f"Empty: {type(object)}")
		case _:
			print("Type not Found")

	if (object != object): return (0)
	if (object): return (1)
	return (0)
