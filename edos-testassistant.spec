%define name edos-testassistant
%define version 1.0.4alpha
%define release %mkrel 4

Summary:	The EDOS Manual Test Assistant
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		https://www.edos-project.org
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


%changelog
* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 1.0.4alpha-4mdv2011.0
+ Revision: 593660
- drop changelog

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4alpha-4mdv2010.0
+ Revision: 437376
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4alpha-3mdv2009.0
+ Revision: 244627
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4alpha-1mdv2008.1
+ Revision: 166602
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu May 24 2007 François Déchelle <fdechelle@mandriva.org> 1.0.4alpha-1mdv2008.0
+ Revision: 30679
- * fixed internationalization
  * fixed path problems

* Tue May 15 2007 François Déchelle <fdechelle@mandriva.org> 1.0.3alpha-1mdv2008.0
+ Revision: 26997
- fixing dependencies
- Fixing dependencies
- changed requires and buildrequires to use %%py_requires

* Thu May 10 2007 François Déchelle <fdechelle@mandriva.org> 1.0.2alpha-2mdv2008.0
+ Revision: 26052
- Fixing 64bits...
- Trying to fix build failed on 64bits
- Initial import of edos-testassistant
- Create edos-testassistant

