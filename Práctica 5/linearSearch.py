def linearSearchUsers(arr, usernameToSearch):
    for i in range(0, len(arr)):
        if arr[i].username == usernameToSearch:
            return i

    return -1
