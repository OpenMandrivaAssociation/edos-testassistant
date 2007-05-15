%define name edos-testassistant
%define version 1.0.3alpha
%define release %mkrel 1

Summary:	The EDOS Manual Test Assistant
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.edos-project.org
License:	GPL
Group:		Development/Python
Source0:	http://www.edos-project.org/releases/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Packager:       Francois Dechelle <fdechelle@mandriva.com>
%py_requires -d
Requires:       edos-testrunner
Requires:	python-pyxml
Requires:       python-kde
Requires:       python-qt

%description
A test assistant developped by the EDOS project, that can run manual tests and report test results using the EDOS test runner.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot} --install-scripts=%{buildroot}/usr/bin --install-lib=%{buildroot}/%python_sitelib
# Remove unpackage egg-info file
rm -rf %{buildroot}/%python_sitelib/edos_testassistant*.egg-info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README 
%python_sitelib/edostestassistant/*.py
%python_sitelib/edostestassistant/*.pyc
%_bindir/edos-testassistant

%changelog
* Thu May 10 2007 Francois Dechelle <fdechelle@mandriva.com>
- changed Requires and BuildRequires to use %py_requires -d
- added removal of unpackaged egg-info file

* Wed Jan 10 2007 Francois Dechelle <fdechelle@mandriva.com>
- moved to setup.py

* Tue Oct 24 2006 Francois Dechelle <fdechelle@mandriva.com>
- initial package

