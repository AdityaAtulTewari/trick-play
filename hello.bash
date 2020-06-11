#!/bin/bash
firefox -CreateProfile $1

MOZ_DIR=~/.mozilla/firefox/$(ls ~/.mozilla/firefox/ --color=never |grep --color=never $1)
PROF_PR=$MOZ_DIR/prefs.js

echo 'user_pref("layers.acceleration.disabled", true);' >> $PROF_PR
echo 'user_pref("dom.allow_scripts_to_close_windows", true);' >> $PROF_PR
echo 'user_pref("media.block-autoplay-until-in-foreground", false);' >> $PROF_PR
echo 'user_pref("media.autoplay.default", 0);' >> $PROF_PR
echo 'user_pref("dom.disable_open_during_load", false);' >> $PROF_PR

killall -9 firefox
