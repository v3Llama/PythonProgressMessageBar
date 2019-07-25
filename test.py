from progress_bar import ProgWithMsg

import time

def important_function():

	important_things = ["important"] * 100

	with ProgWithMsg() as p:
		
		for idx in range(len(important_things)):

			msg = "processing important thing no. {}".format(idx)
			p.update(idx, len(important_things), msg)
			time.sleep(0.1)

if __name__ == "__main__":
	
	important_function()