local wezterm = require 'wezterm'

local config = {}
-- color scheme
config.color_scheme = 'Batman'

config.default_prog = { 'C:\\Program Files\\Git\\bin\\bash.exe', '-l', '-i'}

-- tab bar
config.enable_tab_bar = true
config.use_fancy_tab_bar = false
config.hide_tab_bar_if_only_one_tab = true
config.tab_bar_at_bottom = true

-- window background opacity
config.window_background_opacity = 1

-- Show which key table is active in the status area
wezterm.on('update-right-status', function(window, pane)
    local name = window:active_key_table()
    if name then
        name = 'TABLE: ' .. name
    end
    window:set_right_status(name or '')
end)

-- config.disable_default_key_bindings = true

-- leader key
-- config.leader = { key = 'x', mods = 'CTRL', timeout_milliseconds = 1000 }
local act = wezterm.action
--  key binding
config.keys = {
    { key = 'P',          mods = 'SHIFT|CTRL', action = act.ActivateCommandPalette },
    { key = '`',          mods = 'CTRL',       action = act.SpawnTab 'CurrentPaneDomain' },
    { key = 'Tab',        mods = 'CTRL',       action = act.ActivateTabRelative(1) },
    { key = 'Tab',        mods = 'SHIFT|CTRL', action = act.ActivateTabRelative(-1) },
    { key = 'Backspace',  mods = 'CTRL',       action = act.CloseCurrentTab { confirm = false } },
    { key = 'Enter',      mods = 'ALT',        action = act.ToggleFullScreen },
    { key = '=',          mods = 'CTRL',       action = act.ResetFontSize },
    { key = '+',          mods = 'CTRL',       action = act.IncreaseFontSize },
    { key = '-',          mods = 'CTRL',       action = act.DecreaseFontSize },
    { key = 'c',          mods = 'CTRL|SHIFT', action = act.CopyTo 'Clipboard' },
    { key = 'v',          mods = 'CTRL|SHIFT', action = act.PasteFrom 'Clipboard' },
    { key = 'f',          mods = 'CTRL|SHIFT',       action = act.Search 'CurrentSelectionOrEmptyString' },
    { key = 'c',          mods = 'CTRL|ALT',   action = act.ActivateCopyMode },
    { key = 'Z',          mods = 'CTRL|ALT',   action = act.TogglePaneZoomState },
    { key = 'PageUp',     mods = 'SHIFT',      action = act.ScrollByPage(-1) },
    { key = 'PageDown',   mods = 'SHIFT',      action = act.ScrollByPage(1) },
    { key = '-',          mods = 'ALT',        action = act.SplitVertical { domain = 'CurrentPaneDomain' } },
    { key = '\\',         mods = 'ALT',        action = act.SplitHorizontal { domain = 'CurrentPaneDomain' } },
    { key = 'Backspace',  mods = 'ALT',        action = wezterm.action.CloseCurrentPane { confirm = false } },
    { key = 'LeftArrow',  mods = 'ALT',        action = act.ActivatePaneDirection 'Left' },
    { key = 'RightArrow', mods = 'ALT',        action = act.ActivatePaneDirection 'Right' },
    { key = 'UpArrow',    mods = 'ALT',        action = act.ActivatePaneDirection 'Up' },
    { key = 'DownArrow',  mods = 'ALT',        action = act.ActivatePaneDirection 'Down' },
    { key = 'LeftArrow',  mods = 'CTRL|ALT',   action = act.AdjustPaneSize { 'Left', 1 } },
    { key = 'RightArrow', mods = 'CTRL|ALT',   action = act.AdjustPaneSize { 'Right', 1 } },
    { key = 'UpArrow',    mods = 'CTRL|ALT',   action = act.AdjustPaneSize { 'Up', 1 } },
    { key = 'DownArrow',  mods = 'CTRL|ALT',   action = act.AdjustPaneSize { 'Down', 1 } },

}


wezterm.on('update-right-status', function(window, pane)
    local name = window:active_key_table()
    if name then
        name = 'TABLE: ' .. name
    end
    window:set_right_status(name or '')
end)


return config