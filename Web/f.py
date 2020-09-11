import win32security
import ntsecuritycon as con

FILENAME = "app.py"

userx, domain, type = win32security.LookupAccountName ("", "Isaura")
#usery, domain, type = win32security.LookupAccountName ("", "User Y")

sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()

dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
#dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, usery)

sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)