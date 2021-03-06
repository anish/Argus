#
# Argus web services
#
BuildArch:     noarch
Name:          argusws
Version:       4.3
Release:       1 
License:       GPL+
Group:         Applications/System
Summary:       Argus web services
Distribution:  Salesforce.com, Inc.
Vendor:        Salesforce.com, Inc.
Packager:      Salesforce.com, Inc.
URL:           https://github.com/SalesforceEng/Argus

%define _stagerootdir	%{_buildrootdir}/%{name}-%{version}-%{release}.noarch

%description
Argus is a time-series monitoring and alerting platform.

%prep
rm -rf %{_stagerootdir}
mkdir -p %{_stagerootdir}

%install
pwd
mkdir -p %{_stagerootdir}/%{_targetdir}
cp %{_topdir}/ArgusWebServices/target/argus-webservices-*.war %{_stagerootdir}/%{_targetdir}

%files
/%{_targetdir}
%pre

%post
echo "Installation complete."
