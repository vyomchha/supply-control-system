import time

def scs_check_system():
	print("scs_check_system completed")
	return 0

def scs_update_data():
	print("scs_update_data completed")
	return 0

def scs_update_ui():
	print("scs_update_ui completed")
	return 0

def scs_cloud_update():
	print("scs_cloud_update completed")
	return 0

def scs_start():
	while(1):
		scs_check_system()
		scs_update_data()
		scs_update_ui()
		scs_cloud_update()
		print("loop completed")
		time.sleep(10)

scs_start()