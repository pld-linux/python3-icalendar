%define		module		icalendar
Summary:	iCalendar parser/generator
Name:		python3-%{module}
Version:	5.0.7
Release:	3
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/icalendar/
Source0:	https://files.pythonhosted.org/packages/source/i/icalendar/%{module}-%{version}.tar.gz
# Source0-md5:	338c8791e989554273705e3004843b0d
URL:		https://icalendar.readthedocs.io/
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The icalendar package is a RFC 5545 compatible parser/generator for
iCalendar files.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,CONTRIBUTING,LICENSE,README}.rst
%attr(755,root,root) %{_bindir}/icalendar
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
