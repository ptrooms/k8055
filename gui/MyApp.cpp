#include "MyApp.h"

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    MyFrame *frame = new MyFrame( _T("K8055 USB Experiment Interface Board PtrO"), wxPoint(50,50), wxSize(680,420) );
    frame->Show(TRUE);
    SetTopWindow(frame);
    return TRUE;
} 
