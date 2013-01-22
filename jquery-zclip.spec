# NOTES
# - bundles ZeroClipboard 1.0.7, adds jQuery wrapper
# TODO
# - patch default .swf path?
%define		plugin	zclip
Summary:	jQuery ZeroClipboard
Name:		jquery-%{plugin}
Version:	1.1.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://www.steamdev.com/zclip/archive/jquery.%{plugin}.%{version}.zip
# Source0-md5:	e80f36a66e2c0fbc10454fc78acfea52
URL:		http://www.steamdev.com/zclip/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
zClip is a lightweight jQuery "copy to clipboard" plugin built using
the popular Zero Clipboard library. This plugin uses an invisible
Adobe Flash movie that is fully compatible with Flash Player 10 and
below.

Features:
- Compatible with Flash 10
- Avoids built in browser security conflicts by using a 3rd party
  browser plugin (Adobe Flash)
- Invisible overlay, no interference with page design
- Support for CSS ":hover" and ":active" states
- Preserves the targeted element's "click" "mouseenter" and
  "mouseleave" events
- Supplies callback functions for "before copy" and "after copy"
- Extremely light weight! (~7KB minified)

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p *.swf $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
