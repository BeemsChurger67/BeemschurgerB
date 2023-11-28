Public Class Form1
    Dim moveStep As Integer = 10 ' Amount of movement per key press

    Public Sub New()
        InitializeComponent()
        Me.MaximizeBox = False
        Me.FormBorderStyle = FormBorderStyle.FixedSingle
        Me.KeyPreview = True ' Enable key event handling for the form
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        MsgBox("bruh")
    End Sub

    Private Sub Form1_Resize(sender As Object, e As EventArgs) Handles Me.Resize
        If Me.WindowState = FormWindowState.Maximized Then
            Me.WindowState = FormWindowState.Normal
        End If
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        AddRectangleMovement()
    End Sub

    Private Sub AddRectangleMovement()
        Dim rectPictureBox As New PictureBox()
        rectPictureBox.BackColor = Color.Red
        rectPictureBox.Size = New Size(50, 50)
        rectPictureBox.Location = New Point(0, 0)
        Me.Controls.Add(rectPictureBox)

        AddHandler Me.KeyDown, AddressOf Form1_KeyDown

        Me.Focus()
    End Sub

    Private Sub Form1_KeyDown(sender As Object, e As KeyEventArgs)
        Dim rectPictureBox As PictureBox = Me.Controls.OfType(Of PictureBox)().FirstOrDefault()

        If rectPictureBox IsNot Nothing Then
            Select Case e.KeyCode
                Case Keys.W
                    rectPictureBox.Top -= moveStep
                Case Keys.A
                    rectPictureBox.Left -= moveStep
                Case Keys.S
                    rectPictureBox.Top += moveStep
                Case Keys.D
                    rectPictureBox.Left += moveStep
            End Select
        End If
    End Sub
End Class