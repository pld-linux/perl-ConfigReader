%include	/usr/lib/rpm/macros.perl
Summary:	ConfigReader perl module
Summary(pl):	Modu³ perla ConfigReader
Name:		perl-ConfigReader
Version:	0.5
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	 ftp://ftp.perl.org/pub/CPAN/modules/by-module/ConfigReader/ConfigReader-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConfigReader module for perl.

%description -l pl
Modu³ perla ConfigReader.

%prep
%setup -q -n ConfigReader-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d	$RPM_BUILD_ROOT%{perl_sitelib}/ConfigReader
install *.pm	$RPM_BUILD_ROOT%{perl_sitelib}/ConfigReader

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/ConfigReader
