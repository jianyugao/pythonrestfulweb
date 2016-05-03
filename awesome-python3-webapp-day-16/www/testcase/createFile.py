
import os
import errno

flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
name = "filename"
path = os.path.join("./newDir",name)
try:
    file_handle = os.open(path, flags)
except OSError as e:
    if e.errno == errno.EEXIST:  # Failed as the file already exists.
        print("failed")
        pass
    else:  # Something unexpected went wrong so reraise the exception.
        raise
else:  # No exception, so the file must have been created successfully.
    with os.fdopen(file_handle, 'w') as file_obj:
        # Using `os.fdopen` converts the handle to an object that acts like a
        # regular Python file object, and the `with` context manager means the
        # file will be automatically closed when we're done with it.
        file_obj.write("Look, ma, I'm writing to a new file!")


#http://stackoverflow.com/questions/10978869/safely-create-a-file-if-and-only-if-it-does-not-exist-with-python