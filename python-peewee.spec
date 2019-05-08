#
# Spec base taken from
# https://src.fedoraproject.org/cgit/rpms/python-peewee.git/tree/python-peewee.spec
#

%global pypi_name peewee

Name:		python-%{pypi_name}
Version:	2.10.2
Release:	3%{?dist}
Summary:	A small, expressive orm

License:	MIT
URL:		http://github.com/coleifer/peewee/
Source0:	https://files.pythonhosted.org/packages/7a/bc/aafce76cae9362dccf70e35c16a6cc11d114ebb640bbb86d76255be5c0d6/peewee-2.10.2.tar.gz

BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-Cython

%description
A small, expressive ORM written in python with built-in support for sqlite,
mysql and postgresql and special extensions like hstore. For flask
integration, including an admin interface and RESTful API, check out
flask-peewee.

%package -n python2-%{pypi_name}

Requires:	python-simplejson

Summary:	A small, expressive orm
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
A small, expressive ORM written in python with built-in support for sqlite,
mysql and postgresql and special extensions like hstore. For flask
integration, including an admin interface and RESTful API, check out
flask-peewee.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
#%py2_build
%{__python2} setup.py build


%install
#%py2_install
%{__python2} setup.py install --root=$RPM_BUILD_ROOT
rm %{buildroot}%{python2_sitearch}/pwiz.*
rm %{buildroot}%{_bindir}/pwiz.py

%files -n python2-%{pypi_name}
%license LICENSE
%{python2_sitearch}/peewee.*
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitearch}/playhouse
%{_bindir}/pskel


%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1 (#1448980)

* Mon Apr 10 2017 Viliam Krizan <vkrizan@redhat.com> - 2.9.2-1
- Update to 2.9.2

* Fri Mar 03 2017 Viliam Krizan <vkrizan@redhat.com> - 2.8.8-1
- Update to 2.8.8

* Tue Feb 07 2017 Viliam Krizan <vkrizan@redhat.com> - 2.8.5-2
- Backport upstream fix to force limit and offset to be numeric

* Mon Jan 09 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.8.5-1
- Update to 2.8.5

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-4
- Rebuild for Python 3.6

* Thu Nov 10 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-3
- Make pskel script install under usr/bin/
- Remove bytecompiled pwiz files

* Fri Nov 04 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-2
- Change runtime requirement from python2-simplejson to python-simplejson

* Wed Nov 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-1
- Update to 2.8.2
- Changed the installation directories to be arch dependent as the package
is now compiled using Cython

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-5
- Fix shebangs so python 2 is not dragged with the python 3 subpackage
- Build documentation

* Thu Jun 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-4
- Provide Python 3 subpackage
- Move binaries to Python 3 subpackage
- Modernize SPEC

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Wed Aug 27 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Mon Jun 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.2.4-1
- Update to 2.2.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.1.7-1
- Update to 2.1.7

* Tue Aug 13 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.1.4-2
- Added patch increasing timeout in concurrency test

* Wed Aug 07 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.1.4-1
- Updated to 2.1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.0.9-2
- Review fixes

* Fri Mar 29 2013 mstuchli <mstuchli@redhat.com> - 2.0.9-1
- Initial spec
