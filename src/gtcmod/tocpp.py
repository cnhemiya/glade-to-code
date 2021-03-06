# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-14 12:59
"""

import os
import gtcmod.core as gtcc
import gtcmod.codeobject as gtccb

MAP_GLADE_IDX = gtccb.MAP_GLADE_IDX
MAP_CLASS_IDX = gtccb.MAP_CLASS_IDX
MAP_MOD_IDX = gtccb.MAP_MOD_IDX
GTC_FILE_HEADER = "// " + gtccb.GTC_FILE_HEADER + "\n"

GLADE_MAP_GTK = [
    {MAP_GLADE_IDX: "GFileIcon", MAP_CLASS_IDX: "Gio::FileIcon",
        MAP_MOD_IDX: "<giomm/fileicon.h>"},
    # 未知 {MAP_GLADE_IDX:"GladeInstantiableGtkBin", MAP_CLASS_IDX:"", MAP_MOD_IDX:""},
    {MAP_GLADE_IDX: "GThemedIcon", MAP_CLASS_IDX: "Gio::ThemedIcon",
        MAP_MOD_IDX: "<giomm/themedicon.h>"},
    {MAP_GLADE_IDX: "GtkAboutDialog", MAP_CLASS_IDX: "Gtk::AboutDialog",
        MAP_MOD_IDX: "<gtkmm/aboutdialog.h>"},
    {MAP_GLADE_IDX: "GtkAccelGroup", MAP_CLASS_IDX: "Gtk::AccelGroup",
        MAP_MOD_IDX: "<gtkmm/accelgroup.h>"},
    {MAP_GLADE_IDX: "GtkAccelLabel", MAP_CLASS_IDX: "Gtk::AccelLabel",
        MAP_MOD_IDX: "<gtkmm/accellabel.h>"},
    {MAP_GLADE_IDX: "GtkAction", MAP_CLASS_IDX: "Gtk::Action",
        MAP_MOD_IDX: "<gtkmm/action.h>"},
    {MAP_GLADE_IDX: "GtkActionBar", MAP_CLASS_IDX: "Gtk::ActionBar",
        MAP_MOD_IDX: "<gtkmm/actionbar.h>"},
    {MAP_GLADE_IDX: "GtkActionGroup", MAP_CLASS_IDX: "Gtk::ActionGroup",
        MAP_MOD_IDX: "<gtkmm/actiongroup.h>"},
    {MAP_GLADE_IDX: "GtkAdjustment", MAP_CLASS_IDX: "Gtk::Adjustment",
        MAP_MOD_IDX: "<gtkmm/adjustment.h>"},
    {MAP_GLADE_IDX: "GtkAlignment", MAP_CLASS_IDX: "Gtk::Alignment",
        MAP_MOD_IDX: "<gtkmm/alignment.h>"},
    {MAP_GLADE_IDX: "GtkAppChooserButton", MAP_CLASS_IDX: "Gtk::AppChooserButton",
        MAP_MOD_IDX: "<gtkmm/appchooserbutton.h>"},
    {MAP_GLADE_IDX: "GtkAppChooserDialog", MAP_CLASS_IDX: "Gtk::AppChooserDialog",
        MAP_MOD_IDX: "<gtkmm/appchooserdialog.h>"},
    {MAP_GLADE_IDX: "GtkAppChooserWidget", MAP_CLASS_IDX: "Gtk::AppChooserWidget",
        MAP_MOD_IDX: "<gtkmm/appchooserwidget.h>"},
    {MAP_GLADE_IDX: "GtkApplicationWindow", MAP_CLASS_IDX: "Gtk::ApplicationWindow",
        MAP_MOD_IDX: "<gtkmm/applicationwindow.h>"},
    {MAP_GLADE_IDX: "GtkAspectFrame", MAP_CLASS_IDX: "Gtk::AspectFrame",
        MAP_MOD_IDX: "<gtkmm/aspectframe.h>"},
    {MAP_GLADE_IDX: "GtkAssistant", MAP_CLASS_IDX: "Gtk::Assistant",
        MAP_MOD_IDX: "<gtkmm/assistant.h>"},
    {MAP_GLADE_IDX: "GtkBox", MAP_CLASS_IDX: "Gtk::Box", MAP_MOD_IDX: "<gtkmm/box.h>"},
    {MAP_GLADE_IDX: "GtkButton", MAP_CLASS_IDX: "Gtk::Button",
        MAP_MOD_IDX: "<gtkmm/button.h>"},
    {MAP_GLADE_IDX: "GtkButtonBox", MAP_CLASS_IDX: "Gtk::ButtonBox",
        MAP_MOD_IDX: "<gtkmm/buttonbox.h>"},
    {MAP_GLADE_IDX: "GtkCalendar", MAP_CLASS_IDX: "Gtk::Calendar",
        MAP_MOD_IDX: "<gtkmm/calendar.h>"},
    {MAP_GLADE_IDX: "GtkCheckButton", MAP_CLASS_IDX: "Gtk::CheckButton",
        MAP_MOD_IDX: "<gtkmm/checkbutton.h>"},
    {MAP_GLADE_IDX: "GtkColorButton", MAP_CLASS_IDX: "Gtk::ColorButton",
        MAP_MOD_IDX: "<gtkmm/colorbutton.h>"},
    {MAP_GLADE_IDX: "GtkColorChooserDialog", MAP_CLASS_IDX: "Gtk::ColorChooserDialog",
        MAP_MOD_IDX: "<gtkmm/colorchooserdialog.h>"},
    {MAP_GLADE_IDX: "GtkColorChooserWidget", MAP_CLASS_IDX: "Gtk::ColorChooserWidget",
        MAP_MOD_IDX: "<gtkmm/colorchooserwidget.h>"},
    {MAP_GLADE_IDX: "GtkColorSelection", MAP_CLASS_IDX: "Gtk::ColorSelection",
        MAP_MOD_IDX: "<gtkmm/colorselection.h>"},
    {MAP_GLADE_IDX: "GtkColorSelectionDialog", MAP_CLASS_IDX: "Gtk::ColorSelectionDialog",
        MAP_MOD_IDX: "<gtkmm/colorselection.h>"},
    {MAP_GLADE_IDX: "GtkComboBox", MAP_CLASS_IDX: "Gtk::ComboBox",
        MAP_MOD_IDX: "<gtkmm/combobox.h>"},
    {MAP_GLADE_IDX: "GtkComboBoxText", MAP_CLASS_IDX: "Gtk::ComboBoxText",
        MAP_MOD_IDX: "<gtkmm/comboboxtext.h>"},
    {MAP_GLADE_IDX: "GtkDialog", MAP_CLASS_IDX: "Gtk::Dialog",
        MAP_MOD_IDX: "<gtkmm/dialog.h>"},
    {MAP_GLADE_IDX: "GtkDrawingArea", MAP_CLASS_IDX: "Gtk::DrawingArea",
        MAP_MOD_IDX: "<gtkmm/drawingarea.h>"},
    {MAP_GLADE_IDX: "GtkEntry", MAP_CLASS_IDX: "Gtk::Entry",
        MAP_MOD_IDX: "<gtkmm/entry.h>"},
    {MAP_GLADE_IDX: "GtkEntryBuffer", MAP_CLASS_IDX: "Gtk::EntryBuffer",
        MAP_MOD_IDX: "<gtkmm/entrybuffer.h>"},
    {MAP_GLADE_IDX: "GtkEntryCompletion", MAP_CLASS_IDX: "Gtk::EntryCompletion",
        MAP_MOD_IDX: "<gtkmm/entrycompletion.h>"},
    {MAP_GLADE_IDX: "GtkEventBox", MAP_CLASS_IDX: "Gtk::EventBox",
        MAP_MOD_IDX: "<gtkmm/eventbox.h>"},
    {MAP_GLADE_IDX: "GtkExpander", MAP_CLASS_IDX: "Gtk::Expander",
        MAP_MOD_IDX: "<gtkmm/expander.h>"},
    {MAP_GLADE_IDX: "GtkFileChooserButton", MAP_CLASS_IDX: "Gtk::FileChooserButton",
        MAP_MOD_IDX: "<gtkmm/filechooserbutton.h>"},
    {MAP_GLADE_IDX: "GtkFileChooserDialog", MAP_CLASS_IDX: "Gtk::FileChooserDialog",
        MAP_MOD_IDX: "<gtkmm/filechooserdialog.h>"},
    {MAP_GLADE_IDX: "GtkFileChooserNative", MAP_CLASS_IDX: "Gtk::FileChooserNative",
        MAP_MOD_IDX: "<gtkmm/filechoosernative.h>"},
    {MAP_GLADE_IDX: "GtkFileChooserWidget", MAP_CLASS_IDX: "Gtk::FileChooserWidget",
        MAP_MOD_IDX: "<gtkmm/filechooserwidget.h>"},
    {MAP_GLADE_IDX: "GtkFileFilter", MAP_CLASS_IDX: "Gtk::FileFilter",
        MAP_MOD_IDX: "<gtkmm/filefilter.h>"},
    {MAP_GLADE_IDX: "GtkFixed", MAP_CLASS_IDX: "Gtk::Fixed",
        MAP_MOD_IDX: "<gtkmm/fixed.h>"},
    {MAP_GLADE_IDX: "GtkFlowBox", MAP_CLASS_IDX: "Gtk::FlowBox",
        MAP_MOD_IDX: "<gtkmm/flowbox.h>"},
    {MAP_GLADE_IDX: "GtkFontButton", MAP_CLASS_IDX: "Gtk::FontButton",
        MAP_MOD_IDX: "<gtkmm/fontbutton.h>"},
    {MAP_GLADE_IDX: "GtkFontChooserDialog", MAP_CLASS_IDX: "Gtk::FontChooserDialog",
        MAP_MOD_IDX: "<gtkmm/fontchooserdialog.h>"},
    {MAP_GLADE_IDX: "GtkFontChooserWidget", MAP_CLASS_IDX: "Gtk::FontChooserWidget",
        MAP_MOD_IDX: "<gtkmm/fontchooserwidget.h>"},
    {MAP_GLADE_IDX: "GtkFontSelection", MAP_CLASS_IDX: "Gtk::FontSelection",
        MAP_MOD_IDX: "<gtkmm/fontselection.h>"},
    {MAP_GLADE_IDX: "GtkFontSelectionDialog", MAP_CLASS_IDX: "Gtk::FontSelectionDialog",
        MAP_MOD_IDX: "<gtkmm/fontselection.h>"},
    {MAP_GLADE_IDX: "GtkFrame", MAP_CLASS_IDX: "Gtk::Frame",
        MAP_MOD_IDX: "<gtkmm/frame.h>"},
    {MAP_GLADE_IDX: "GtkGLArea", MAP_CLASS_IDX: "Gtk::GLArea",
        MAP_MOD_IDX: "<gtkmm/glarea.h>"},
    {MAP_GLADE_IDX: "GtkGrid", MAP_CLASS_IDX: "Gtk::Grid",
        MAP_MOD_IDX: "<gtkmm/grid.h>"},
    {MAP_GLADE_IDX: "GtkHandleBox", MAP_CLASS_IDX: "Gtk::HandleBox",
        MAP_MOD_IDX: "<gtkmm/handlebox.h>"},
    {MAP_GLADE_IDX: "GtkHeaderBar", MAP_CLASS_IDX: "Gtk::HeaderBar",
        MAP_MOD_IDX: "<gtkmm/headerbar.h>"},
    {MAP_GLADE_IDX: "GtkIconFactory", MAP_CLASS_IDX: "Gtk::IconFactory",
        MAP_MOD_IDX: "<gtkmm/iconfactory.h>"},
    {MAP_GLADE_IDX: "GtkIconView", MAP_CLASS_IDX: "Gtk::IconView",
        MAP_MOD_IDX: "<gtkmm/iconview.h>"},
    {MAP_GLADE_IDX: "GtkImage", MAP_CLASS_IDX: "Gtk::Image",
        MAP_MOD_IDX: "<gtkmm/image.h>"},
    {MAP_GLADE_IDX: "GtkInfoBar", MAP_CLASS_IDX: "Gtk::InfoBar",
        MAP_MOD_IDX: "<gtkmm/infobar.h>"},
    {MAP_GLADE_IDX: "GtkLabel", MAP_CLASS_IDX: "Gtk::Label",
        MAP_MOD_IDX: "<gtkmm/label.h>"},
    {MAP_GLADE_IDX: "GtkLayout", MAP_CLASS_IDX: "Gtk::Layout",
        MAP_MOD_IDX: "<gtkmm/layout.h>"},
    {MAP_GLADE_IDX: "GtkLevelBar", MAP_CLASS_IDX: "Gtk::LevelBar",
        MAP_MOD_IDX: "<gtkmm/levelbar.h>"},
    {MAP_GLADE_IDX: "GtkLinkButton", MAP_CLASS_IDX: "Gtk::LinkButton",
        MAP_MOD_IDX: "<gtkmm/linkbutton.h>"},
    {MAP_GLADE_IDX: "GtkListBox", MAP_CLASS_IDX: "Gtk::ListBox",
        MAP_MOD_IDX: "<gtkmm/listbox.h>"},
    {MAP_GLADE_IDX: "GtkListStore", MAP_CLASS_IDX: "Gtk::ListStore",
        MAP_MOD_IDX: "<gtkmm/liststore.h>"},
    {MAP_GLADE_IDX: "GtkLockButton", MAP_CLASS_IDX: "Gtk::LockButton",
        MAP_MOD_IDX: "<gtkmm/lockbutton.h>"},
    {MAP_GLADE_IDX: "GtkMenu", MAP_CLASS_IDX: "Gtk::Menu",
        MAP_MOD_IDX: "<gtkmm/menu.h>"},
    {MAP_GLADE_IDX: "GtkMenuBar", MAP_CLASS_IDX: "Gtk::MenuBar",
        MAP_MOD_IDX: "<gtkmm/menubar.h>"},
    {MAP_GLADE_IDX: "GtkMenuButton", MAP_CLASS_IDX: "Gtk::MenuButton",
        MAP_MOD_IDX: "<gtkmm/menubutton.h>"},
    {MAP_GLADE_IDX: "GtkMessageDialog", MAP_CLASS_IDX: "Gtk::MessageDialog",
        MAP_MOD_IDX: "<gtkmm/messagedialog.h>"},
    {MAP_GLADE_IDX: "GtkModelButton", MAP_CLASS_IDX: "Gtk::ModelButton",
        MAP_MOD_IDX: "<gtkmm/modelbutton.h>"},
    {MAP_GLADE_IDX: "GtkNotebook", MAP_CLASS_IDX: "Gtk::Notebook",
        MAP_MOD_IDX: "<gtkmm/notebook.h>"},
    {MAP_GLADE_IDX: "GtkOffscreenWindow", MAP_CLASS_IDX: "Gtk::OffscreenWindow",
        MAP_MOD_IDX: "<gtkmm/offscreenwindow.h>"},
    {MAP_GLADE_IDX: "GtkOverlay", MAP_CLASS_IDX: "Gtk::Overlay",
        MAP_MOD_IDX: "<gtkmm/overlay.h>"},
    {MAP_GLADE_IDX: "GtkPaned", MAP_CLASS_IDX: "Gtk::Paned",
        MAP_MOD_IDX: "<gtkmm/paned.h>"},
    {MAP_GLADE_IDX: "GtkPlacesSidebar", MAP_CLASS_IDX: "Gtk::PlacesSidebar",
        MAP_MOD_IDX: "<gtkmm/placessidebar.h>"},
    {MAP_GLADE_IDX: "GtkPopover", MAP_CLASS_IDX: "Gtk::Popover",
        MAP_MOD_IDX: "<gtkmm/popover.h>"},
    {MAP_GLADE_IDX: "GtkPopoverMenu", MAP_CLASS_IDX: "Gtk::PopoverMenu",
        MAP_MOD_IDX: "<gtkmm/popovermenu.h>"},
    {MAP_GLADE_IDX: "GtkProgressBar", MAP_CLASS_IDX: "Gtk::ProgressBar",
        MAP_MOD_IDX: "<gtkmm/progressbar.h>"},
    {MAP_GLADE_IDX: "GtkRadioAction", MAP_CLASS_IDX: "Gtk::RadioAction",
        MAP_MOD_IDX: "<gtkmm/radioaction.h>"},
    {MAP_GLADE_IDX: "GtkRadioButton", MAP_CLASS_IDX: "Gtk::RadioButton",
        MAP_MOD_IDX: "<gtkmm/radiobutton.h>"},
    {MAP_GLADE_IDX: "GtkRecentAction", MAP_CLASS_IDX: "Gtk::RecentAction",
        MAP_MOD_IDX: "<gtkmm/recentaction.h>"},
    {MAP_GLADE_IDX: "GtkRecentChooserDialog", MAP_CLASS_IDX: "Gtk::RecentChooserDialog",
        MAP_MOD_IDX: "<gtkmm/recentchooserdialog.h>"},
    {MAP_GLADE_IDX: "GtkRecentChooserMenu", MAP_CLASS_IDX: "Gtk::RecentChooserMenu",
        MAP_MOD_IDX: "<gtkmm/recentchoosermenu.h>"},
    {MAP_GLADE_IDX: "GtkRecentChooserWidget", MAP_CLASS_IDX: "Gtk::RecentChooserWidget",
        MAP_MOD_IDX: "<gtkmm/recentchooserwidget.h>"},
    {MAP_GLADE_IDX: "GtkRecentFilter", MAP_CLASS_IDX: "Gtk::RecentFilter",
        MAP_MOD_IDX: "<gtkmm/recentfilter.h>"},
    {MAP_GLADE_IDX: "GtkRecentManager", MAP_CLASS_IDX: "Gtk::RecentManager",
        MAP_MOD_IDX: "<gtkmm/recentmanager.h>"},
    {MAP_GLADE_IDX: "GtkRevealer", MAP_CLASS_IDX: "Gtk::Revealer",
        MAP_MOD_IDX: "<gtkmm/revealer.h>"},
    {MAP_GLADE_IDX: "GtkScale", MAP_CLASS_IDX: "Gtk::Scale",
        MAP_MOD_IDX: "<gtkmm/scale.h>"},
    {MAP_GLADE_IDX: "GtkScaleButton", MAP_CLASS_IDX: "Gtk::caleButton",
        MAP_MOD_IDX: "<gtkmm/scalebutton.h>"},
    {MAP_GLADE_IDX: "GtkScrollbar", MAP_CLASS_IDX: "Gtk::Scrollbar",
        MAP_MOD_IDX: "<gtkmm/scrollbar.h>"},
    {MAP_GLADE_IDX: "GtkScrolledWindow", MAP_CLASS_IDX: "Gtk::ScrolledWindow",
        MAP_MOD_IDX: "<gtkmm/scrolledwindow.h>"},
    {MAP_GLADE_IDX: "GtkSearchBar", MAP_CLASS_IDX: "Gtk::SearchBar",
        MAP_MOD_IDX: "<gtkmm/searchbar.h>"},
    {MAP_GLADE_IDX: "GtkSearchEntry", MAP_CLASS_IDX: "Gtk::SearchEntry",
        MAP_MOD_IDX: "<gtkmm/searchentry.h>"},
    {MAP_GLADE_IDX: "GtkSeparator", MAP_CLASS_IDX: "Gtk::Separator",
        MAP_MOD_IDX: "<gtkmm/separator.h>"},
    {MAP_GLADE_IDX: "GtkSizeGroup", MAP_CLASS_IDX: "Gtk::SizeGroup",
        MAP_MOD_IDX: "<gtkmm/sizegroup.h>"},
    {MAP_GLADE_IDX: "GtkSpinButton", MAP_CLASS_IDX: "Gtk::SpinButton",
        MAP_MOD_IDX: "<gtkmm/spinbutton.h>"},
    {MAP_GLADE_IDX: "GtkSpinner", MAP_CLASS_IDX: "Gtk::Spinner",
        MAP_MOD_IDX: "<gtkmm/spinner.h>"},
    {MAP_GLADE_IDX: "GtkStack", MAP_CLASS_IDX: "Gtk::Stack",
        MAP_MOD_IDX: "<gtkmm/stack.h>"},
    {MAP_GLADE_IDX: "GtkStackSidebar", MAP_CLASS_IDX: "Gtk::StackSidebar",
        MAP_MOD_IDX: "<gtkmm/stacksidebar.h>"},
    {MAP_GLADE_IDX: "GtkStackSwitcher", MAP_CLASS_IDX: "Gtk::StackSwitcher",
        MAP_MOD_IDX: "<gtkmm/stackswitcher.h>"},
    {MAP_GLADE_IDX: "GtkStatusbar", MAP_CLASS_IDX: "Gtk::Statusbar",
        MAP_MOD_IDX: "<gtkmm/statusbar.h>"},
    {MAP_GLADE_IDX: "GtkStatusIcon", MAP_CLASS_IDX: "Gtk::StatusIcon",
        MAP_MOD_IDX: "<gtkmm/statusicon.h>"},
    {MAP_GLADE_IDX: "GtkSwitch", MAP_CLASS_IDX: "Gtk::Switch",
        MAP_MOD_IDX: "<gtkmm/switch.h>"},
    {MAP_GLADE_IDX: "GtkTable", MAP_CLASS_IDX: "Gtk::Table",
        MAP_MOD_IDX: "<gtkmm/table.h>"},
    {MAP_GLADE_IDX: "GtkTextBuffer", MAP_CLASS_IDX: "Gtk::TextBuffer",
        MAP_MOD_IDX: "<gtkmm/textbuffer.h>"},
    {MAP_GLADE_IDX: "GtkTextTag", MAP_CLASS_IDX: "Gtk::TextTag",
        MAP_MOD_IDX: "<gtkmm/texttag.h>"},
    {MAP_GLADE_IDX: "GtkTextTagTable", MAP_CLASS_IDX: "Gtk::TextTagTable",
        MAP_MOD_IDX: "<gtkmm/texttagtable.h>"},
    {MAP_GLADE_IDX: "GtkTextView", MAP_CLASS_IDX: "Gtk::TextView",
        MAP_MOD_IDX: "<gtkmm/textview.h>"},
    {MAP_GLADE_IDX: "GtkToggleAction", MAP_CLASS_IDX: "Gtk::ToggleAction",
        MAP_MOD_IDX: "<gtkmm/toggleaction.h>"},
    {MAP_GLADE_IDX: "GtkToggleButton", MAP_CLASS_IDX: "Gtk::ToggleButton",
        MAP_MOD_IDX: "<gtkmm/togglebutton.h>"},
    {MAP_GLADE_IDX: "GtkToolbar", MAP_CLASS_IDX: "Gtk::Toolbar",
        MAP_MOD_IDX: "<gtkmm/toolbar.h>"},
    {MAP_GLADE_IDX: "GtkToolPalette", MAP_CLASS_IDX: "Gtk::ToolPalette",
        MAP_MOD_IDX: "<gtkmm/toolpalette.h>"},
    {MAP_GLADE_IDX: "GtkTreeModelFilter", MAP_CLASS_IDX: "Gtk::TreeModelFilter",
        MAP_MOD_IDX: "<gtkmm/treemodelfilter.h>"},
    {MAP_GLADE_IDX: "GtkTreeModelSort", MAP_CLASS_IDX: "Gtk::TreeModelSort",
        MAP_MOD_IDX: "<gtkmm/treemodelsort.h>"},
    {MAP_GLADE_IDX: "GtkTreeStore", MAP_CLASS_IDX: "Gtk::TreeStore",
        MAP_MOD_IDX: "<gtkmm/treestore.h>"},
    {MAP_GLADE_IDX: "GtkTreeView", MAP_CLASS_IDX: "Gtk::TreeView",
        MAP_MOD_IDX: "<gtkmm/treeview.h>"},
    {MAP_GLADE_IDX: "GtkViewport", MAP_CLASS_IDX: "Gtk::Viewport",
        MAP_MOD_IDX: "<gtkmm/viewport.h>"},
    {MAP_GLADE_IDX: "GtkVolumeButton", MAP_CLASS_IDX: "Gtk::VolumeButton",
        MAP_MOD_IDX: "<gtkmm/volumebutton.h>"},
    {MAP_GLADE_IDX: "GtkWindow", MAP_CLASS_IDX: "Gtk::Window",
        MAP_MOD_IDX: "<gtkmm/window.h>"},
    {MAP_GLADE_IDX: "GtkWindowGroup", MAP_CLASS_IDX: "Gtk::WindowGroup",
        MAP_MOD_IDX: "<gtkmm/windowgroup.h>"}
]


class ToCpp(gtccb.CodeObject):
    """
    转 C++ 代码
    """

    def __init__(self):
        super().__init__()

    def makeCode(self):
        """
        生成代码，公有权限方便调试

        Returns:
            str: 生成的代码
        """
        code = self.__srcFileBegin()
        code += self.__srcModule()
        code += self.__srcGladeString()
        code += self.__srcCodeBegin()
        code += self.__srcCodeMain()
        code += self.__srcCodeEnd()
        code += self.__srcFileEnd()
        return code

    def __srcFileBegin(self):
        """
        生成代码，文件开始
        """
        name = self._gladeBaseName.upper()
        code = GTC_FILE_HEADER + "\n"
        code += "#ifndef _" + name + "_H_\n"
        code += "#define _" + name + "_H_\n"
        code += "\n"
        return code

    def __srcModule(self):
        """
        生成代码，模块
        """
        code = "#include <assert.h>\n"
        code += "#include <glibmm/ustring.h>\n"
        code += "#include <gtkmm/builder.h>\n"
        code += self._modListCode("#include ", GLADE_MAP_GTK)
        return code

    def __srcGladeString(self):
        """
        生成代码，Glade 文件内容
        """
        old_new = {"\'": "\\\'", "\"": "\\\""}
        code = "const Glib::ustring "
        code += self._gladeBaseName + "_glade_string = \"\\\n"
        lines = gtcc.replaceStringByDict(self._gladeTxt, old_new)
        for i in lines.split("\n"):
            code += i + "\\\n"
        code += "\";\n\n"
        return code

    def __srcCodeBegin(self):
        """
        生成代码，代码开始
        """
        code = "class " + self._gladeBaseName + " : public Gtk::Container\n{\n"
        code += "public:\n"
        return code

    def __srcCodeMain(self):
        """
        生成代码，主代码
        """
        space = "    "
        code = space + self._gladeBaseName + "()\n"
        code += space + "{\n"
        code += self.__builderCode() + "\n"
        code += self.__assertCode()
        code += space + "}\n\n"
        code += self.__objecCode()
        return code

    def __builderCode(self):
        """
        生成代码，builder
        """
        space = "        "
        code = space + "builder = Gtk::Builder::create_from_string(" \
            + self._gladeBaseName + "_glade_string);\n"
        for i in self._gladeParse.classAndId:
            glade_map = self._gladeMapGtk(
                i[gtcc.XML_ATTRIB_CLASS], GLADE_MAP_GTK)
            id = i[gtcc.XML_ATTRIB_ID]
            code += space + "builder->get_widget<" + glade_map[1] \
                + ">(\"" + id + "\", " + id + ");\n"
        return code

    def __assertCode(self):
        """
        生成代码，断言
        """
        space = "        "
        code = ""
        for i in self._gladeParse.classAndId:
            code += space + \
                "assert(" + i[gtcc.XML_ATTRIB_ID] + " != nullptr);\n"
        return code

    def __objecCode(self):
        """
        生成代码，对象列表
        """
        space = "    "
        code = space + "Glib::RefPtr<Gtk::Builder> builder;\n"
        for i in self._gladeParse.classAndId:
            glade_map = self._gladeMapGtk(
                i[gtcc.XML_ATTRIB_CLASS], GLADE_MAP_GTK)
            code += space + glade_map[1] + " *" + \
                i[gtcc.XML_ATTRIB_ID] + ";\n"
        return code

    def __srcCodeEnd(self):
        """
        生成代码，代码结束
        """
        code = "};\n\n"
        return code

    def __srcFileEnd(self):
        """
        生成代码，文件结束
        """
        code = "#endif"
        return code
