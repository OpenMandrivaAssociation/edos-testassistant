%define name edos-testassistant
%define version 1.0.4alpha
%define release %mkrel 4

Summary:	The EDOS Manual Test Assistant
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.edos-project.org
License:	GPL
Group:		Development/Python
Source0:	http://www.edos-project.org/releases/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BUildRequires:	python
Requires:       edos-testrunner
Requires:	python-pyxml
Requires:       python-kde
Requires:       python-qt

%description
A test assistant developped by the EDOS project, that can run manual tests and
report test results using the EDOS test runner.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot} --install-scripts=%{buildroot}%{_bindir} --install-lib=%{buildroot}/%{python_sitelib} --install-data=%{buildroot}%{_datadir}
# Remove unpackage egg-info file
rm -rf %{buildroot}/%{python_sitelib}/edos_testassistant*.egg-info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README 
%{python_sitelib}/edostestassistant/*.py
%{_bindir}/edos-testassistant
%{_datadir}/edos-testassistant/translations/TestAssistant_*.qm
