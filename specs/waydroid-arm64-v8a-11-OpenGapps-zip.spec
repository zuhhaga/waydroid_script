BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-arm64-v8a-11-OpenGapps-zip
Source0: https://sourceforge.net/projects/opengapps/files/arm64/20220503/open_gapps-arm64-11.0-pico-20220503.zip
%build_waydroid_extra_from_file gapps.zip 11/gapps.zip arm64-v8a/11/gapps.zip
