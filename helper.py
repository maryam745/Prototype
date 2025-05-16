import flet as ft


theme_main_color = ft.Colors.BLACK
theme_secondary_color = ft.Colors.YELLOW_700

#alert dialogue
def show_alert(title,message,page):

    dlg = ft.AlertDialog(
            title=ft.Icon(name=ft.icons.ERROR, color=ft.Colors.WHITE, size=100),
            content=ft.Column(
                [
                    ft.Text(value=title, size=20, weight=ft.FontWeight.BOLD, color='white'),
                    
                    ft.Text(value=message, color='white', text_align="center"),
                ], horizontal_alignment="center", height=60
            ),
            actions=[
                ft.Container(height=30),
                ft.FilledButton(
                    "Close", width=400,
                    
                    style=ft.ButtonStyle(
                        bgcolor='white', color=ft.Colors.BLUE_900,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click= lambda _:close_dialog(page)
                     
                )           
            ],
            bgcolor=theme_main_color,
            shape=ft.RoundedRectangleBorder(radius=5),
            content_padding=10
        )
    page.open(dlg)
    page.update()

def show_alert_sucess(title,message,page):

    dlg = ft.AlertDialog(
            title=ft.Icon(name=ft.icons.CHECK, color=ft.Colors.WHITE, size=100),
            content=ft.Column(
                [
                    ft.Text(value=title, size=20, weight=ft.FontWeight.BOLD, color='white'),
                    
                    ft.Text(value=message, color='white', text_align="center"),
                ], horizontal_alignment="center", height=60
            ),
            actions=[
                ft.Container(height=30),
                ft.FilledButton(
                    "Close", width=400,
                    
                    style=ft.ButtonStyle(
                        bgcolor='white', color=ft.Colors.BLUE_900,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click= lambda _:close_dialog(page)
                     
                )           
            ],
            bgcolor=theme_main_color,
            shape=ft.RoundedRectangleBorder(radius=5),
            content_padding=0
        )
    page.open(dlg)
    page.update()

def close_dialog(page):
    #print("Calling Close Dialog")
    #print("Current Overlay:", page.overlay)  # Debug the overlay
    if page.overlay:  # Check if there are any dialogs in the overlay
        try:
            for dialog in page.overlay:
                dialog.open = False  # Close all dialogs in the overlay
            page.update()  # Ensure the UI updates
            #print("All dialogs closed successfully.")
        except Exception as e:
            print(f"Failed to close dialogs: {e}")
    else:
        print("")
        
#alert box
def show_alert_box(title,message,page):

    dlg = ft.AlertDialog(
            title=ft.Row(
            [
                ft.IconButton(ft.Icons.CLOSE, on_click=lambda _: close_dialog(page)),
                
            ],
            alignment=ft.MainAxisAlignment.END
        ),
            content=ft.Column(
                [
                    ft.Text(value=title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text(value=message),
                ],
                width=800,height=600,
                scroll=ft.ScrollMode.HIDDEN
            ),
            actions=[
                      
            ],
            
            modal=True,
            bgcolor=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=5),
            
        )
    page.open(dlg)
    page.update()

def show_alert_box_content(data,page):

    dlg = ft.AlertDialog(
            title=ft.Row(
            [
                ft.IconButton(ft.Icons.CLOSE,icon_color=theme_main_color,
                               on_click=lambda _: close_dialog(page)),
                
            ],
            alignment=ft.MainAxisAlignment.END
        ),
            content=data,
            actions=[
                      
            ],
            
            #modal=True,
            #bgcolor=theme_main_color,
            shape=ft.RoundedRectangleBorder(radius=5),
            scrollable=True,
            inset_padding=2
            
        )
    page.open(dlg)
    page.update()

#alert loading rinf
def show_alert_loading_ring(color,page):

    dlg = ft.AlertDialog(
             content=ft.Container(
                 
                content=ft.ProgressRing(
                    color=color,
                    tooltip=ft.Tooltip(
                        message="Loading"
                    ),
                    
                    ),
            
            alignment=ft.alignment.center
                
            ),
            actions=[
                      
            ],
            
            #modal=True,
            bgcolor=ft.Colors.TRANSPARENT,
            shape=ft.RoundedRectangleBorder(radius=5),
            
        )
    page.open(dlg)
    page.update()

#alert loading progress
def show_alert_loading_progress(color,page):

    dlg = ft.AlertDialog(
             content=ft.Container(
                 
                content=ft.ProgressBar(
                    color=color,
                    tooltip=ft.Tooltip(
                        message="Loading"
                    ),
                    bgcolor='black'
                    
                    ),
            
            alignment=ft.alignment.center
                
            ),
            actions=[
                      
            ],
            
            #modal=True,
            bgcolor=ft.Colors.TRANSPARENT,
            shape=ft.RoundedRectangleBorder(radius=5),
            
        )
    page.open(dlg)
    page.update()



#bottom sheet 
def show_bottom_sheet(title,message,page):
    bs = ft.BottomSheet(
        
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value=title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=message),
                ],
                expand=True
            ),
            padding=20,
            width=1000
        ),
        bgcolor='white',
        use_safe_area=True,
    
        
    )

    page.open(bs)
    page.update()

#bottom sheet with content 
def show_bottom_sheet_content(data,page):
    bs = ft.BottomSheet(
        
        content= ft.Container(
            content=data,
            padding=20,
            width=1000,
            visible=True,
            #height=1800
            expand=True
        ),
        use_safe_area=True,
        visible=True,
        bgcolor='white',
        enable_drag=True,
        is_scroll_controlled=True
        
        
        
     
        
    )

    page.open(bs)
    page.update()

#banner 
def show_banner(color,message,page):
    bs = ft.Banner(
        bgcolor=color,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED,color='white', size=40),
        content=ft.Text(
            value=message,color='white',
        ),
        actions=[
            ft.IconButton(icon=ft.icons.CLOSE,icon_color='white',
                          on_click= lambda _: page.close(bs))
        ],
        content_padding=10,
    )

    page.open(bs)
    page.update()


# Create a ProgressBar instance with a label
ring = ft.ProgressBar(
    visible=True,
    color=ft.Colors.YELLOW_800,
    semantics_label="Loading Data",  # Static label for accessibility
)

box = ft.Container(
    content=ft.Column(
        [
            ft.Text("Processing Data"),
            ring
        ],horizontal_alignment="center"
    ),visible=False,padding=20
)

# Function to show the loader
def show_loader(color):
    box.visible = True
    box.content.controls[0].color = color
    return box

# Function to hide the loader
def hide_loader():
    box.visible = False
    return box

#assets

def bottom_bar(on_change_callback):
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CHAT, label="Chats", data="0"),
            ft.NavigationBarDestination(icon=ft.Icons.GROUP, label="Rooms", data="1"),
            ft.NavigationBarDestination(icon=ft.Icons.CREATE_ROUNDED, label="Bots", data="2"),
            ft.NavigationBarDestination(icon=ft.Icons.ACCOUNT_BOX, label="Account", data="3"),
        ],
        on_change=on_change_callback,
    )
