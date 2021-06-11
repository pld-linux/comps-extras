Summary:	Images for package groups
Name:		comps-extras
Version:	24
Release:	1
License:	GPL+ and LGPLv2+ and GPLv2+ and CC-BY-SA and MIT
Source0:	https://releases.pagure.org/comps-extras/%{name}-%{version}.tar.gz
# Source0-md5:	a5ccd3bf632517769f62105a880fe0ef
URL:		https://pagure.io/comps-extras
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains images for the components included in a
distribution.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc comps.dtd comps-cleanup.xsl
%doc COPYING
%{_pixmapsdir}/comps
